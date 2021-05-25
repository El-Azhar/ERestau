


$.ajax({
    url: '/cart/ajax/',
    type: 'get',
    data: {
        action: 'get_total_cart',
    },
    success: function(response){
        var total = response.total
        var nb_articles = response.nb_articles

        $("td#total-price").text(total + " Dhs")
    }
})