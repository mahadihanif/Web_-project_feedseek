from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    POST_CHOICES = (
        ('D', 'Want to donate',),
        ('R', 'Request for donate',),
        
    )

    post_choice = models.CharField(max_length=20,choices=POST_CHOICES) 
    food_name = models.CharField(max_length=150,blank=True)
    organization_name = models.CharField(max_length=50,blank=True)
    how_many_people = models.IntegerField(blank=True)
    date = models.DateField(blank=True)
    location = models.CharField(max_length=70,blank=True)
    add_note = models.TextField(max_length=500,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.food_name} Post'
    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})