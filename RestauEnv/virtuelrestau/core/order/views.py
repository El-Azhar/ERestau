from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from core.order.forms import OrderForm
from core.models import Product, Category, Order, SelectedProduct, IdOrder
from core.cart.views import get_total_cart, cart_clear, update_cart_items


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

    form = OrderForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name})
    current_user = request.user

    defaut_firstname = current_user.first_name
    defaut_lastname = current_user.last_name

    # print("current_user: " +str(current_user))
    # print("defaut_firstname: " + str(defaut_firstname))
    # print("defaut_lastname: " + str(defaut_lastname))

    extra_context = {
        "form": form,
        "defaut_firstname": defaut_firstname,
        "defaut_lastname": defaut_lastname,
    }

    return render(request, 'order/order.html', extra_context)

@login_required()
def order_preparation(request):
    # extra_context = {"order_id: ": request.order_id}
    extra_context = {}
    return render(request, 'order/order_preparation.html', extra_context)

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
                price = float(curr_product.price),
                quantity = int(curr_dict_val.get('quantity')),
                order_id = new_order_id,
            )
            selected_product.save()

            list_selected_products.append(selected_product)
    # print("list_selected_products de la fonction: " + str(list_selected_products))
    return list_selected_products

class AjaxOrderView(View):
    def get(self, request):
        print(request.GET)
        if request.is_ajax():
            action = request.GET.get('action')

            if action == "confirm_order":
                order_id = int(request.GET.get('order_id'))
                print("order_id: " + str(order_id))
                orders = Order.objects.filter(order_id=order_id)

                for order in orders:
                    order.is_confirmed = True
                    order.save()

                #On vide la panier
                cart_clear(request)
                return  JsonResponse({}, status=200)

            elif action == 'new_order' :
                last_name  = request.GET.get('last_name')
                first_name  = request.GET.get('first_name')
                adresse  = request.GET.get('adresse')
                phone_number  = request.GET.get('phone_number')

                # print("request.user: " + str(request.user))
                # print("type of request.user: " + str(type(request.user)))

                new_id_order = IdOrder(user=request.user)
                new_id_order.save()
                # print("new_id_order: " + str(new_id_order.id))
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
                                      price = float(selected_product.price) * float(selected_product.quantity),
                                      )
                    new_order.save()

                return JsonResponse({'order_id': str(new_id_order.id)}, status=200)

            elif action == 'change_order' :
                last_name  = request.GET.get('last_name')
                first_name  = request.GET.get('first_name')
                adresse  = request.GET.get('adresse')
                phone_number  = request.GET.get('phone_number')

                order_id  = request.GET.get('order_id')
                # print("new_id_order: " + str(new_id_order.id))
                list_selected_products = SelectedProduct.objects.filter(order_id=order_id)
                list_order = Order.objects.filter(order_id=order_id)

                for order in list_order:
                    order.last_name = last_name
                    order.first_name = first_name
                    order.phone_number = phone_number
                    order.adresse = adresse
                    order.save()

                return JsonResponse({'order_id': order_id}, status=200)

        return render(request, 'order/order.html')