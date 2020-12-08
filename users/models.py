from django.db import models
#from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    full_name = models.CharField(max_length=150, blank=True)
    phone = PhoneNumberField(blank=True)
    #phone_number = PhoneField(blank=True, help_text='Contact phone number')
    address = models.TextField(max_length=30, blank=True)
    

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)