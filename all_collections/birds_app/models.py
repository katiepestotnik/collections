from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your models here.
class Bird(models.Model):
  species=models.CharField(max_length=100)
  colors=ArrayField(
    ArrayField(
      models.CharField(max_length=30, blank=True)
    )
  )
  location=models.CharField(max_length=200)
  notes=models.TextField()
  date=models.DateField()
  url = models.CharField(max_length=300)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.species} is {self.colors}'