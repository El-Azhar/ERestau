from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from core.order.forms import OrderForm
from core.models import Product, Category


@login_required()
def home(request):
    return redirect(reverse('customer:profile'))

@login_required()
def ouazzane_page(request):
    if "next_category" in request.GET:
        next_category = request.GET["next_category"]
        products = list(Product.objects.filter(category=Category.objects.get(name=next_category)))

    else:
        next_category = ""
        products = list(Product.objects.all())

    extra_context = {"products": products,"next_category": next_category }
    return render(request, 'ouazzane/ouazzane.html', extra_context)


@login_required()
def order(request):

    # cart = Cart(request)
    # nb_articles = 0
    # for curr_dict_val in cart.cart.values():
    #     curr_quantity = int(curr_dict_val.get('quantity'))
    #     if curr_quantity > 0:
    #         nb_articles += 1

    form = OrderForm()
    current_user = request.user

    defaut_firstname = current_user.first_name
    defaut_lastname = current_user.last_name

    print("current_user: " +str(current_user))
    print("defaut_firstname: " + str(defaut_firstname))
    print("defaut_lastname: " + str(defaut_lastname))

    extra_context = {
        "form": form,
        "defaut_firstname": defaut_firstname,
        "defaut_lastname": defaut_lastname,
    }

    return render(request, 'order/order.html', extra_context)
