from django.db import models
from django.contrib.postgres.fields import ArrayField
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

  def __str__(self):
    return f'{self.species} is {self.colors}'