const form_client = document.querySelectorAll(".form-client");
const btn_valid_customer_form = document.querySelector(".button-form");
document.quer
function isNumeric(value) {
    return /^-?\d+$/.test(value);
}

btn_valid_customer_form.addEventListener('click', e =>{
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

        create_new_order(last_name, first_name, first_name, phone_number)

    } else{

        var last_name = $("#id_last_name").val();
        var first_name = $("#id_first_name").val();
        var adresse = $("#id_adresse").val();
        var phone_number = $("#id_phone_number").val();

        change_informations_order(order_id, last_name, first_name, adresse, phone_number)

    }

})