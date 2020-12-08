from django.urls import path
#from .views import PostListView
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
]