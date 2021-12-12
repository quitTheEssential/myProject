from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

BRAND_CHOICES = (
    ('A','Adidas'),
    ('N','Nike'),
)

class Products(models.Model):
    Product_ID = models.AutoField(primary_key=True, db_index=True)
    brand = models.TextField(choices=BRAND_CHOICES,max_length=100,default='')
    model = models.TextField(max_length=100,default='')
    size = models.DecimalField(max_digits=3, decimal_places=1,default='')
    price = models.DecimalField(max_digits=6,decimal_places=2, default='')
    colour = models.TextField(max_length=15,default='')
    Picture = models.ImageField(default='default.jpg', upload_to='product_pics')

    def __str__(self):
        return self.model

    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)
        img = Image.open(self.Picture.path)

        if img.height > 1 or img.width > 1:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.Picture.path)

class Orders(models.Model):
    Order_ID = models.AutoField(primary_key=True, db_index = True)
    Client_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Product_ID = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.Order_ID