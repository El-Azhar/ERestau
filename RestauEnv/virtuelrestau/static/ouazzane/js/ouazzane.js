const retour_popup_cart = document.querySelector(".retour-popup-cart")
/* var ex_id= "remove_product_cart_2"
console.log(ex_id.split('_'))
console.log(btn) */

update_page_numbers()

const btn_add_product = document.querySelectorAll(".logo-plus");
btn_add_product.forEach((item) => {

    item.addEventListener('click', (e)=>{
        product_id = e.target.id;
        add_product_cart(product_id)
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


function  update_item(){
    $('.cart-card-items').html('').load("/update_cart_items")
}

var button_cart = document.querySelector("#cart-button")
button_cart.addEventListener('click', e=>{
    update_item()
})


var btn_clear_cart =document.querySelector("#clear-cart")
btn_clear_cart.addEventListener('click', e=>{
    clear_cart()
})



