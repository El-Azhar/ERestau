"""virtuelrestau URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib.auth import views as auth_views

from core import views
from core.cart.views import AjaxHandlerView
from core.order import views as order_views
from core.cart import views as cart_views



urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),

    path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/')),
    path('sign-up', views.sign_up),
    path('track-menu/', views.track_order_page),

]

order_urlpattern = [
    path(r'order/', order_views.order_page, name='order')
]

cart_urlpatterns = [
    path('cart/add/<int:id>/', cart_views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', cart_views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         cart_views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         cart_views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',cart_views.cart_detail,name='cart_detail'),
]

ajax_url_patterns = [
    path('cart/ajax/', AjaxHandlerView.as_view())
]

urlpatterns = urlpatterns + order_urlpattern + cart_urlpatterns + ajax_url_patterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
