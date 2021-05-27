var btn_add_product_cart = document.querySelectorAll(".logo-plus-cart");
btn_add_product_cart.forEach((item) => {
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

var btn_remove_product_cart = document.querySelectorAll(".logo-moins-cart");
btn_remove_product_cart.forEach((item) => {
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