
function change_informations_order(order_id, last_name, first_name, adresse, phone_number){
    var last_name = $("#id_last_name").val();
    var first_name = $("#id_first_name").val();
    var adresse = $("#id_adresse").val();
    var phone_number = $("#id_phone_number").val();
    $.ajax({
        url: 'new_order/',
        type: 'get',
        data: {
            action: 'change_order',
            last_name :last_name,
            first_name  :first_name,
            adresse :adresse,
            phone_number : phone_number,
            order_id: order_id,
        },
        success: function(response){
            var order_id = response.order_id
            $("td#order-number").text( order_id)
        }
    })
}

function create_new_order(last_name, first_name, first_name, phone_number){
    $.ajax({
        url: 'new_order/',
        type: 'get',
        data: {
            action: 'new_order',
            last_name :last_name,
            first_name  :first_name,
            adresse :first_name,
            phone_number : phone_number,
        },
        success: function(response){
            var order_id = response.order_id
            $("td#order-number").text( order_id)
        }
    })
}