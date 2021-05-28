
function update_cart_nb_articles(){
    $.ajax({
        url: '/cart/ajax/',
        type: 'get',
        data: {
            action: 'update_nb_articles_cart',
        },
        success: function(response){
            var nb_articles = response.nb_articles
            $("#cercle_nb_articles").text(nb_articles)
        }
    })
}

function update_cart_total_price(){
    $.ajax({
        url: '/cart/ajax/',
        type: 'get',
        data: {
            action: 'update_total_cart',
        },

        success: function(response){
            var total = response.total
            $("p#total-price").text(total + ' Dhs')
        }

    })
}

function update_page_numbers(){
    update_cart_nb_articles()
    update_cart_total_price()
}

function clear_cart() {

    $.ajax({
        url: '/cart/ajax/',
        type: 'get',
        data: {
            action: 'clear_cart',
        },
        success: function (response) {
            $('.modal').modal('hide')
            // $("#cercle_nb_articles").text('0')
            // $("p#total-price").text(0 + " Dhs")
            update_cart_nb_articles()
            update_cart_total_price()
        }
    })

}

function add_product_cart(product_id){

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

            $("p#quantity_prod_" + id).text('x' + quantity)

            update_cart_nb_articles()
            update_cart_total_price()

        }
    })

}

function remove_product_cart(product_id){
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

            $("p#quantity_prod_" + id).text('x' + quantity)

            update_cart_nb_articles()
            update_cart_total_price()

        }
    })
}


