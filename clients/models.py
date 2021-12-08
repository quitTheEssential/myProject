from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, default=' ')
    surname = models.TextField(max_length=100, default=' ')
    email = models.EmailField( default=' ')
    telephone = models.CharField(max_length=9, default=' ')
    city = models.TextField(max_length=100, default=' ')
    street = models.TextField(max_length=100, default=' ')
    street_number = models.TextField(max_length=10, default=' ')
    flat_number = models.TextField(max_length=10, default=' ')
    postal_code = models.TextField(max_length=6, default='')
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

#reducing a pictures files size
    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (1000,1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

