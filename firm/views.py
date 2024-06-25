from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from firm.models import Firm
from users.models import User, UserRole
from django.views import View
from firm.forms import FirmRegistrationForm
# messages framework
from django.contrib import messages

# Email configuration Imports
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode

from django.utils.encoding import force_bytes
from django.utils.encoding import force_str

from django.contrib.auth.tokens import default_token_generator


# class FirmListView(LoginRequiredMixin, View):
#     def get(self, request):
#         firms = Firm.objects.filter(user=request.user)
#         return render(request, 'firms/firm_list.html', {'firms': firms})


class FirmCreateView(View):
    template_name = 'firm/register_firm.html'
    form_class = FirmRegistrationForm

    def get(self, request, *args, **kwargs):
        # form = self.form_class()
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Extract and manipulate company_phone_no
        company_phone_no = request.POST.get('company_phone_no', '')
        full_personal_phone = request.POST.get('full_personal_phone', '')
        if company_phone_no:
            # company_phone_no = company_phone_no[-1]

            split_parts = company_phone_no.split('+', 2)  # Limiting to split at most 2 times
            
            if len(split_parts) >= 3:
                actual_phone_number = split_parts[2]

                # Create a mutable copy of request.POST
                mutable_post = request.POST.copy()
                # Update the mutable copy with the manipulated phone number
                mutable_post['company_phone_no'] = actual_phone_number
                # Replace request.POST with the updated mutable copy
                request.POST = mutable_post

            else:
                actual_phone_number = None  # Handle case where split does not yield expected parts

        if full_personal_phone:
            # company_phone_no = company_phone_no[-1]

            split_parts = full_personal_phone.split('+', 2)  # Limiting to split at most 2 times
            
            if len(split_parts) >= 3:
                actual_phone_number = split_parts[2]

                # Create a mutable copy of request.POST
                mutable_post = request.POST.copy()
                # Update the mutable copy with the manipulated phone number
                mutable_post['owner_phone_no'] = actual_phone_number
                # Replace request.POST with the updated mutable copy
                request.POST = mutable_post

            else:
                actual_phone_number = None  # Handle case where split does not yield expected parts



        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                password = request.POST['password']
                confirm_password = request.POST['confirm_password']

                # Check if passwords match
                if password != confirm_password:
                    raise ValueError("Passwords do not match.")                
                    
                # Create User
                user = User.objects.create(
                    username=form.cleaned_data['owner_name'],
                    email=form.cleaned_data['poc_email'],
                    password=password,
                    role=UserRole.objects.get(role_name='Firms')
                )

                # Set the hashed password
                user.set_password(password)
                # Save the user instance to the database
                user.save()

                # Create Firm associated with the User
                firm = form.save(commit=False)
                firm.user = user
                firm.save()

                
                # add status in Firm status history for tracking
                firm.firm_status_change('Pending')


                # Send verification email
                send_verification_email(request, user, form.cleaned_data['poc_email'])

                messages.success(request, 'Firm registered successfully! Please check your email to verify your account.')

                return redirect('login')

            except ValueError as ve:
                # Handle specific password validation errors
                if 'password' in str(ve).lower():
                    messages.error(request, f'Invalid password: {ve}')
                else:
                    messages.error(request, f'An error occurred: {ve}')

                return render(request, self.template_name, {'form': form})

            except Exception as e:
                messages.error(request, f'An error occurred: {e}')

                return render(request, self.template_name, {'form': form})
        else:
            # Collect and display field-specific errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

            # messages.error(request, 'Invalid Data! ')
            return render(request, self.template_name)


def send_verification_email(request, user, email):
    current_site = get_current_site(request)
    mail_subject = 'Activate your firm account'
    message = render_to_string('firm/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    send_mail(
        mail_subject,
        message,
        'msdqhabib@gmail.com',
        [email],
        fail_silently=False,
    )
    print(f'send_mail - {send_mail}')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    firm_instance = Firm.objects.filter(user=user).last()
    if firm_instance.status != "Verified":
        if user is not None and default_token_generator.check_token(user, token):
            firm_instance = Firm.objects.filter(user=user).last()

            # add status in firm status history
            firm_instance.firm_status_change('Verified')
            # Set status to Verified
            firm_instance.status = 'Verified'
            firm_instance.save()


            user.is_active = True
            user.save()
            messages.success(request, 'Your account has been activated successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Activation link is invalid!')
            return render(request, 'activation_invalid.html')


# In case the firm user has not received the activation link
@login_required
def resend_verification_email(request):
    if request.method == 'POST':
        user = request.user
        email = user.email

        # Send verification email
        send_verification_email(request, user, email)

        messages.info(request, 'Verification email has been resent. Please check your email.')

        return redirect('dashboard')
    else:
        return HttpResponseNotAllowed(['POST'])


def faqs(request):
    return render(request, 'firm/faqs.html')
