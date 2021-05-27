const form_client = document.querySelectorAll(".form-client");
const btn_valid_customer_form = document.querySelectorAll(".button-form");

console.log(form_client.values())
console.log(btn_valid_customer_form)

function isNumeric(value) {
    return /^-?\d+$/.test(value);
}

btn_valid_customer_form[0].addEventListener('click', e =>{
    var last_name = $("#id_last_name").val();
    var first_name = $("#id_first_name").val();
    var adresse = $("#id_adresse").val();
    var phone_number = $("#id_phone_number").val();
     // On stocke l'adresse saisie dans le reçu de paiment
    $("td#product-adresse").text(adresse)
    // On récupère le numéro de commande
    var order_id = $("td#order-number").text();
    // Si le numéro de commande n'existe pas on crée une nouvelle commande
    if(!isNumeric(order_id) ){
        $.ajax({
            url: 'new_order/',
            type: 'get',
            data: {
                action: 'new_order',
                last_name :last_name,
                first_name  :first_name,
                adresse :adresse,
                phone_number : phone_number,
            },
            success: function(response){
                var order_id = response.order_id
                $("td#order-number").text( order_id)
            }
        })
    } else{
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

})