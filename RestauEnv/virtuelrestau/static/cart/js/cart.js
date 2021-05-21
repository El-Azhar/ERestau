//var btn_plus_cart = document.querySelectorAll("#logo-plus-cart, #logo-minus-cart");
//
//btn_plus_cart.forEach((item) => {
//    item.addEventListener('click', (e)=>{
//    product_id = e.target.id;
//
//    console.log("from cart.js");
//    console.log("product_id: " + product_id);
//
//
//        $.ajax({
//        url: '/cart/ajax/',
//        type: 'get',
//        data: {
//            action: 'add_product_cart',
//            id: product_id
//        },
//        success: function(response){
//            var name = response.name ;
//            var quantity = response.quantity ;
//            var price = response.price ;
//            var id = response.id
//
//            console.log("name: " + name)
//            console.log("quantity: " + quantity)
//            console.log("price: " + price)
//            console.log("id: " + id)
//            $("#text-quantity-product-" + id + ".col-md-6.text-quantity").text('x' + quantity)
//        }
//        })
//    })
//
//})