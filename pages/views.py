from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})


def about(request):
    return render(request, 'pages/about.html', {})


def contact(request):
    return render(request, 'pages/contact.html', {})    


def gallery(request):
    return render(request, 'pages/gallery.html', {})


@login_required
def home(request):
    return render(request, 'pages/home.html', {})



# class PostListView(ListView):
#     model = Post
#     template_name = 'pages/home.htmml'