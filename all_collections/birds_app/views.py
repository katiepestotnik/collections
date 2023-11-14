from django.shortcuts import render
from django.views.generic import ListView

from .models import Bird
# Create your views here.
# def home(request):
#   return render(request, 'home.html')

class BirdList(ListView):
  #default context bird_list
  model = Bird