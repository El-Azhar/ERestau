console.log("run ouazzane.js")
const total_price = document.querySelector("#cercle_nb_articles");
const retour_popup_cart = document.querySelector(".retour-popup-cart")
/* var ex_id= "remove_product_cart_2"
console.log(ex_id.split('_'))
console.log(btn) */

console.log(total_price)

$.ajax({
    url: '/cart/ajax/',
    type: 'get',
    data: {
        action: 'get_total_cart',
    },
    success: function(response){
        var total = response.total
        var nb_articles = response.nb_articles

        $("p#total-price").text(total + " Dhs")
        $("#cercle_nb_articles").text(nb_articles)

    }
})

const btn_add_product = document.querySelectorAll(".logo-plus");
btn_add_product.forEach((item) => {
    item.addEventListener('click', (e)=>{
    product_id = e.target.id;

    console.log("product_id: " + product_id);

        $.ajax({
        url: '/cart/ajax/',
        type: 'get',
        data: {
            action: 'add_product',
            id: product_id
        },
        success: function(response){
            var name = response.name ;
            var quantity = response.quantity ;
            var price = response.price ;
            var id = response.id
            var total = response.total
            var nb_articles = response.nb_articles

/*            console.log("name: " + name)
            console.log("quantity: " + quantity)
            console.log("price: " + price)
            console.log("id: " + id)*/

            $("p#quantity_prod_" + id).text('x' + quantity)
            $("p#total-price").text(total + " Dhs")
            $("#cercle_nb_articles").text(nb_articles)

        }
        })
    })

})

const btn_remove_product = document.querySelectorAll(".logo-moins");
btn_remove_product.forEach((item) => {
    item.addEventListener('click', (e)=>{
        product_id = e.target.id;

        console.log("product_id: " + product_id);


        $.ajax({
            url: '/cart/ajax/',
            type: 'get',
            data: {
                action: 'remove_product',
                id: product_id
            },
            success: function(response){
                var name = response.name ;
                var quantity = response.quantity ;
                var price = response.price ;
                var id = response.id
                var total = response.total

/*
                console.log("name: " + name)
                console.log("quantity: " + quantity)
                console.log("price: " + price)
                console.log("id: " + id)
*/

                $("p#quantity_prod_" + id).text('x' + quantity)
                $("p#total-price").text(total + " Dhs")
            }
        })
    })

})

retour_popup_cart.addEventListener('click', e =>{
    $('.modal').modal('hide')
})


function update_popup(){
    $('.cart-card-items').html('').load("/update_popup_carts")
}

function  update_item(){
    $('.cart-card-items').html('').load("/update_cart_items")
}

var button_cart = document.querySelector("#cart-button")
button_cart.addEventListener('click', e=>{
    update_item()
    console.log("update item executed")
    // update_popup()
})


// const button_cart = document.querySelector("#cart-button")
// button_cart.addEventListener('click', e=>{
//     $("#popup.modal").reload()
// })const button_cart = document.querySelector("#cart-button")
// // button_cart.addEventListener('click', e=>{
// //     $("#popup.modal").reload()
// // })






//btn.addEventListener('click', function(e){
//    img.classList.toggle('show');
//    console.log(e)
//})

//console.log('after funcion') ;

//$(document).ready(function({
//    $(".btn").click(function(){
//    $.ajax({
//        url: '',
//        type: 'get',
//        data: {
//            text: "il s'agit de mon texte"
//        },
//        success: function(response){
//        console.log("sucess response")
//        }
//        })
//    })
//})
//)