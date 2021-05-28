var btn_add_product_cart = document.querySelectorAll(".logo-plus-cart");
btn_add_product_cart.forEach((item) => {
    item.addEventListener('click', (e)=>{
        product_id = e.target.id;
        add_product_cart(product_id)
    })

})

var btn_remove_product_cart = document.querySelectorAll(".logo-moins-cart");
btn_remove_product_cart.forEach((item) => {
    item.addEventListener('click', (e)=>{
        product_id = e.target.id;
        remove_product_cart(product_id)
    })

})



