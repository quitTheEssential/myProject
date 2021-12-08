from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, default='TBU')
    surname = models.TextField(max_length=100, default='TBU')
    email = models.EmailField( default='TBU')
    sex = models.TextField(max_length=1, default='TBU')
    telephone = models.CharField(max_length=9, default='TBU')
    city = models.TextField(max_length=100, default='TBU')
    street = models.TextField(max_length=100, default='TBU')
    street_number = models.TextField(max_length=10, default='TBU')
    flat_number = models.TextField(max_length=10, default='TBU')
    postal_code = models.TextField(max_length=6, default='TBU')
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'