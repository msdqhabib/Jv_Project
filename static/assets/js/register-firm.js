  var current = 0;
  var tabs = $(".tab");
  var tabs_pill = $(".tab-pills");
  
  loadFormData(current);
  
  function loadFormData(n) {
    $(tabs_pill[n]).addClass("active");
    $(tabs[n]).removeClass("d-none");
    $("#back_button").attr("disabled", n == 0 ? true : false);
    if (n == tabs.length - 1) {
      $("#next_button").text("Submit").attr("onclick", "submitForm()");
    } else {
      $("#next_button").text("Next").attr("onclick", "next()");
    }
  }
  
  function next() {
    $(tabs[current]).addClass("d-none");
    $(tabs_pill[current]).removeClass("active");
  
    current++;
    loadFormData(current);
  }
  
  function back() {
    $(tabs[current]).addClass("d-none");
    $(tabs_pill[current]).removeClass("active");
  
    current--;
    loadFormData(current);
  }


  function submitForm() {
    console.log("fxn callled")
    if ($("#next_button").text() === "Submit") {
     

      $("form.card").submit();
    }
  }
  
  
  $(document).ready(function() {
    $('#same_personal_info').change(function() {
        if ($(this).prop('checked')) {
            // Copy values from personal details tab to POC info tab
            var ownerName = $('input[name="owner_name"]').val();
            var ownerEmail = $('input[name="owner_email"]').val();
            var ownerAddress = $('textarea[name="owner_address"]').val();

            $('input[name="poc_name"]').val(ownerName);
            $('input[name="poc_email"]').val(ownerEmail);
            $('textarea[name="poc_address"]').val(ownerAddress);
        } else {
            // Clear values if checkbox is unchecked
            $('input[name="poc_name"]').val('');
            $('input[name="owner_email"]').val('');
            $('textarea[name="poc_address"]').val('');
        }
    });
});


