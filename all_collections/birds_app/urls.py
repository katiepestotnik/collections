from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.BirdList.as_view(), name='home')
]