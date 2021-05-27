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
    return render(request, 'cart/cart_popup.html')

@login_required()
def update_popup_carts(request):
    cart = Cart(request)
    items = cart.cart.items
    return render(request, 'cart/cart_popup.html',  {'items': items})

@login_required()
def update_cart_items(request):
    cart = Cart(request)
    items = cart.cart.items
    print("items: " + str(items))
    return render(request, 'cart/cart_card_items.html', {'items': items})

@login_required()
def get_total_cart(request):
    cart = Cart(request)

    total = 0
    for curr_dict_val in cart.cart.values():
        total += float(curr_dict_val.get('quantity')) * float(curr_dict_val.get('price'))

    return total\

@login_required()
def get_nb_articles(request):
    cart = Cart(request)

    nb_articles = 0
    for curr_dict_val in cart.cart.values():
        curr_quantity = int(curr_dict_val.get('quantity'))
        if curr_quantity > 0:
            nb_articles += 1
    return nb_articles

class AjaxCartView(View):

    def get(self, request):
        if request.is_ajax():
            action = request.GET.get('action')

            if action == 'add_product' :
                if 'add_product_cart_' in request.GET.get('id'):
                    id = str(request.GET.get('id')).split('add_product_cart_')[1]
                else:
                    id = request.GET.get('id')

                try:
                    cart_add(request, id)
                    print("cart add ok")
                except:
                    return Exception("CARD_ADD ERROR")
            elif action == 'remove_product' :

                if 'remove_product_cart_' in request.GET.get('id'):
                    id = str(request.GET.get('id')).split('remove_product_cart_')[1]
                else:
                    id = request.GET.get('id')

                # print("id in request remove_product_cart_: " + str(id))

                item_decrement(request, id)

            elif action == 'get_total_cart':
                total = get_total_cart(request)
                nb_articles = get_nb_articles(request)
                # print('{"total": total, "nb_articles":nb_articles}: ' + str({"total": total, "nb_articles":nb_articles}))
                return JsonResponse({"total": total, "nb_articles":nb_articles}, status=200)

            values = list(request.session.get('cart').values())

            for product_dict in values:
                curr_id = str(product_dict.get('product_id'))
                if curr_id != id:
                    continue
                else:
                    quantity = product_dict.get("quantity")
                    price = product_dict.get("price")
                    name = product_dict.get("name")

            total = get_total_cart(request)
            nb_articles = get_nb_articles(request)

            dict_response = {
                'name': name,
                'price': price,
                'quantity': quantity,
                'id': id,
                'total': total,
                'nb_articles': nb_articles,
            }

            return JsonResponse(dict_response, status=200)

        return render(request, 'ouazzane/ouazzane.html')

