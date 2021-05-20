from django.db import models

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