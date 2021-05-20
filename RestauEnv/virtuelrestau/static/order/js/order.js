const img = document.getElementById("img");
const btn = document.querySelectorAll(".logo-plus");

const cart_info= document.querySelectorAll(".cart-info");

//const product_name= document.querySelectorAll(".product-name");
//const product_price= document.querySelectorAll(".product-price");
//const product_total= document.querySelectorAll(".product-total");
//const product_total= document.querySelectorAll(".product-total");




btn.forEach((item) => {
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

            console.log("name: " + name)
            console.log("quantity: " + quantity)
            console.log("price: " + price)
            console.log("id: " + id)
            $(".product_" + id + "_quantity").text(quantity)
        }
        })
    })

})

cart_info.forEach((item) =>{

})






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