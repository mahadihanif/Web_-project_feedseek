from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django import forms
from django.urls import reverse
# Create your models here.



class DonatePost(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    food_name = models.CharField(max_length=100, blank=True)
    organization_name = models.CharField(max_length=100, blank=True)
    how_many_people = models.IntegerField(blank=True) 
    #date = models.DateField(blank=True)
    location=models.CharField(max_length=100, blank= True)
    add_note = models.TextField(max_length=500, blank=True)



    def __str__(self):
        return f'{self.food_name} Post'


    # def get_absolute_url(self):
    #     return reverse('home', kwargs={'pk': self.pk})