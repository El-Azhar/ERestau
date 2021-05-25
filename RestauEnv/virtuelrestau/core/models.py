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

class Order(models.Model):
    CONFIRMEE = "confirmer"
    NON_CONFIRMEE = "non-confirmer"
    STATUSES = (
        (CONFIRMEE, 'Confirmée'),
        (NON_CONFIRMEE, 'Non confirmée'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    products = models.ManyToManyField(Category)
    status = models.CharField(max_length=20, choices=STATUSES, default=NON_CONFIRMEE)
