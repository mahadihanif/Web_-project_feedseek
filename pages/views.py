from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from donate_post.models import Post

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})


def about(request):
    return render(request, 'pages/about.html', {})


def contact(request):
    return render(request, 'pages/contact.html', {})    


def gallery(request):
    return render(request, 'pages/gallery.html', {})



# def home(request):
#     return render(request, 'pages/home.html', {})



@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'pages/home.html', context)

