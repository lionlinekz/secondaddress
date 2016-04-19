$("#shipment_number").change(function() {
    var a = parseInt($("#shipment_number option:selected").text());
    var price = a*4.99;
    $("#shipment_price").text("for €"+price.toString());
});
