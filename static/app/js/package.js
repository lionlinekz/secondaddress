$( document ).ready(function() {
                $(this).find("#keepcheck").hide();
                $(this).find("#goldcheck").hide();  
                $(this).find("#goldinfo").hide(); 
                $(this).find("#silverinfo").hide(); 
                $("#firstprice").text("€9.81");
            });
            $('#myForm').click(function() {
               if($('#silver_button').is(':checked')) { 
               $(this).find("#goldname").hide();
                $(this).find("#goldnumber").hide(); 
                $(this).find("#platinumname").hide();
                $(this).find("#platinumnumber").hide();
                $(this).find("#keepcheck").show(); 
                $(this).find("#goldcheck").hide(); 
                $(this).find("#goldinfo").hide(); 
                $(this).find("#platinuminfo").hide(); 
                $(this).find("#silverinfo").show();
                $("#firstprice").text("€4.89"); 
                 }
               if($('#gold_button').is(':checked')) { 
                $(this).find("#goldname").show();
                $(this).find("#goldnumber").show();
                $(this).find("#platinumname").hide();
                $(this).find("#platinumnumber").hide();
                $(this).find("#keepcheck").hide();
                $(this).find("#goldcheck").show(); 
                $(this).find("#goldinfo").show(); 
                $(this).find("#platinuminfo").hide(); 
                $(this).find("#silverinfo").hide();
                $("#firstprice").text("€6.79");    }
               if($('#platinum_button').is(':checked')) {
                $(this).find("#goldname").show();
                $(this).find("#goldnumber").show();
                $(this).find("#goldcheck").hide();  
                $(this).find("#platinumname").show();
                $(this).find("#platinumnumber").show();
                $(this).find("#keepcheck").hide();
                $(this).find("#goldinfo").hide(); 
                $(this).find("#platinuminfo").show(); 
                $(this).find("#silverinfo").hide(); 
                $("#firstprice").text("€9.81"); 
            }
            });
            $("#first").change(function() {
                if(this.checked) {
                    $("#firstprice").text("€6.38");
                    //Do stuff
                }else{
                    $("#firstprice").text("€4.89");
                }
            });
            $("#second").change(function() {
                if(this.checked) {
                    $("#firstprice").text("€8.68");
                    //Do stuff
                }else{
                    $("#firstprice").text("€6.79");
                }
            });
