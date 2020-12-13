from django.shortcuts import render, redirect
#from django.views.generic.base import TemplateView
#from .forms import DonatePostForm
from django.contrib.auth.models import User
from .models import DonatePost
from users.models import Profile
from django.contrib import messages
# Create your views here.


# class DonatePostView(TemplateView):
#     template_name = 'donate_food.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         #fm = DonatePostForm()
#         #context = {'form': fm}
#         context = {}
#         return context

    
        
def donate_food(request,id):
    if request.method == 'POST':
        aid = user.objects.get(pk=id)
        food_name = request.POST['foodname']
        organization_name = request.POST['orgname']
        how_many_people = request.POST['no_of_people']
        #date = request.POST['date']
        location = request.POST['Location']
        add_note = request.POST['info']
        d_post = DonatePost(food_name=food_name,organization_name=organization_name,how_many_people=how_many_people,location=location,add_note=add_note,author=aid)

        d_post.save()
    return render(request, 'donate_food.html', {})
        
        
         
        
        



#     return render(request, 'donate_food.html', {})


def seeking_food(request):

    return render(request, 'seeking_food.html', {})


# class SeekingFoodView(TemplateView):
#     template_name = 'seeking_food.html'