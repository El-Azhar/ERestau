from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from core.models import Product, Category


@login_required()
def home(request):
    return redirect(reverse('customer:profile'))

@login_required()
def order_page(request):
    if "next_category" in request.GET:
        next_category = request.GET["next_category"]
        products = list(Product.objects.filter(category=Category.objects.get(name=next_category)))

    else:
        next_category = ""
        products = list(Product.objects.all())

    extra_context = {"products": products,"next_category": next_category }
    return render(request, 'order/order.html', extra_context)

