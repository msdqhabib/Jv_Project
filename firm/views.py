from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from firm.models import Firm
from users.models import User, UserRole
from django.views import View
from firm.forms import FirmRegistrationForm

from django.contrib import messages


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
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                password = request.POST['password']
                print(f'password - {password}')
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

                messages.success(request, 'Firm registered successfully!')
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
