from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Products(models.Model):
    Product_ID = models.AutoField(primary_key=True, db_index=True , default=1)
    brand = models.TextField(max_length=100,default='')
    model = models.TextField(max_length=100,default='')
    size = models.DecimalField(max_digits=3, decimal_places=1,default='')
    price = models.FloatField(default='')
    colour = models.TextField(max_length=15,default='')
    Picture = models.ImageField(default='default.jpg', upload_to='product_pics')

    def __str__(self):
        return self.model

class Orders(models.Model):
    Order_ID = models.AutoField(primary_key=True, db_index = True, default=1)
    Client_ID = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Product_ID = models.ForeignKey(Products, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.Order_ID