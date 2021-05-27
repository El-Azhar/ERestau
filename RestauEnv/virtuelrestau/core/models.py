from django.utils import timezone
import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Product(models.Model):
    INDISPONIBLE = 'indisponible'
    DISPONIBLE = 'disponible'
    STATUSES = (
        (INDISPONIBLE, 'Indisponible'),
        (DISPONIBLE, 'Disponible'),
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(default=0)
    photo = models.ImageField(upload_to='menu/photo/', default='photo/default.jpg')
    image = models.ImageField(upload_to='products/', default='photo/default.jpg')
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUSES, default=INDISPONIBLE)
    def __str__(self):
        return self.name

class SelectedProduct(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    order_id = models.IntegerField(default=0)
    def __str__(self):
        str_selected_products = str(self.quantity) + "x " + self.name
        return str_selected_products



class Order(models.Model):
    LIVRER = "livrer"
    NON_LIVRER = "non-livrer"
    STATUSES = (
        (LIVRER, 'Livrée'),
        (NON_LIVRER, 'Non livrée'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    selected_product = models.ForeignKey(SelectedProduct, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUSES, default=NON_LIVRER)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    order_id = models.IntegerField(default=0, editable=False)
    price = models.IntegerField(default=0)
def __str__(self):
        str_order = self.first_name + self.last_name
        return str_order

class IdOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
