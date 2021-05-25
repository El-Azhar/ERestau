const form_client = document.querySelectorAll(".form-client");
const btn_valid_customer_form = document.querySelectorAll(".button-form");

console.log(form_client.values())
console.log(btn_valid_customer_form)

btn_valid_customer_form[0].addEventListener('click', e =>{
    var last_name = $("#id_last_name").val();
    var first_name = $("#id_first_name").val();
    var adresse = $("#id_adresse").val();
    var phone_number = $("#id_phone_number").val();

    $("td#text-price").text(adresse)

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

        }
    })
})