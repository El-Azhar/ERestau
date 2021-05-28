

$.ajax({
    url: '/cart/ajax/',
    type: 'get',
    data: {
        action: 'update_total_cart',
    },
    success: function(response){
        var total = response.total
        var nb_articles = response.nb_articles

        $("td#total-price").text(total + " Dhs")
    }
})

const btn_confirm_command = document.querySelector("a#confirm-command");
console.log(btn_confirm_command)
btn_confirm_command.addEventListener('click',  e=>{
    //On récupère d'abord l'id de notre commande
    var order_id = $("td#order-number").text();
    $.ajax({
        url: 'new_order/',
        type: 'get',
        data: {
            action: "confirm_order",
            order_id: order_id,
        },
        success: function(response){

        }
    })
})
