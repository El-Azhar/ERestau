from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from core.order.forms import OrderForm
from core.models import Product, Category, Order, SelectedProduct, IdOrder


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

@login_required()
def get_selected_articles(request, new_order_id):
    cart = Cart(request)
    nb_articles = 0
    list_selected_products = []
    for curr_dict_val in cart.cart.values():
        curr_quantity = int(curr_dict_val.get('quantity'))

        if curr_quantity > 0:
            curr_product_id = curr_dict_val.get('product_id')
            curr_product = Product.objects.get(id=curr_product_id)

            selected_product = SelectedProduct(
                user = request.user,
                name = curr_product.name,
                category = curr_product.category,
                price = curr_product.price,
                quantity = int(curr_dict_val.get('quantity')),
                order_id = new_order_id
            )
            selected_product.save()

            list_selected_products.append(selected_product)
    print("list_selected_products de la fonction: " + str(list_selected_products))
    return list_selected_products

class AjaxOrderView(View):
    def get(self, request):
        print(request.GET)
        if request.is_ajax():
            action = request.GET.get('action')

            if action == 'new_order' :
                last_name  = request.GET.get('last_name')
                first_name  = request.GET.get('first_name')
                adresse  = request.GET.get('adresse')
                phone_number  = request.GET.get('phone_number')

                print("request.user: " + str(request.user))
                print("type of request.user: " + str(type(request.user)))

                new_id_order = IdOrder(user=request.user)
                new_id_order.save()
                print("new_id_order: " + str(new_id_order.id))
                list_selected_products = get_selected_articles(request, new_id_order.id)
                print(list_selected_products)
                for selected_product in list_selected_products:
                    new_order = Order(last_name=last_name,
                                      first_name = first_name,
                                      adresse = adresse,
                                      phone_number = phone_number,
                                      user = request.user,
                                      selected_product = selected_product,
                                      order_id = new_id_order.id,
                                      )
                    new_order.save()

        return JsonResponse({}, status=200)