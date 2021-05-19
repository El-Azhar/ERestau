from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from core.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart



@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/order")

@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

class AjaxHandlerView(View):

    def get(self, request):
        print(request.GET)
        if request.is_ajax():
            action = request.GET.get('action')
            if action == 'add_product':
                id = str(request.GET.get('id'))
                print("id: " + str(id))
                cart_add(request, id)
                values = list(request.session.get('cart').values())
                for product_dict in values:

                    curr_id = str(product_dict.get('product_id'))
                    if curr_id != id:
                        continue

                    quantity = product_dict.get("quantity")
                    price = product_dict.get("price")
                    name = product_dict.get("name")



                dict_response = {
                    'name': name,
                    'price': price,
                    'quantity': quantity,
                    'id': id
                }

            return JsonResponse(dict_response, status=200)

        return render(request, 'order/order.html')
