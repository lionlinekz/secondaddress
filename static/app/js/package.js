$('#myForm').click(function() {
   if($('#silver_button').is(':checked')) { 
   $(this).find("#goldname").hide();
    $(this).find("#goldnumber").hide(); 
    $(this).find("#platinumname").hide();
    $(this).find("#platinumnumber").hide(); 
     }
   if($('#gold_button').is(':checked')) { 
    $(this).find("#goldname").hide();
    $(this).find("#goldnumber").hide();
    $(this).find("#platinumname").show();
    $(this).find("#platinumnumber").show();   }
   if($('#platinum_button').is(':checked')) {
    $(this).find("#goldname").show();
    $(this).find("#goldnumber").show(); 
    $(this).find("#platinumname").show();
    $(this).find("#platinumnumber").show(); 
  }
});
