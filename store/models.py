from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Clients(models.Model):
    ID = models.IntegerField(primary_key = True, db_index = True)
    name = models.TextField(max_length = 100)
    surname = models.TextField(max_length = 100)
    email = models.EmailField()
    sex = models.TextField(max_length = 1)
    telephone = models.CharField(max_length = 9)
    city = models.TextField(max_length=100)
    street = models.TextField(max_length=100)
    street_number = models.TextField(max_length=10)
    flat_number = models.TextField(max_length=10)
    postal_code = models.TextField(max_length=6)

    def __str__(self):
        return self.name