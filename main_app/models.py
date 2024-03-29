from django.db import models
from django.urls import reverse

# Create your models here.
class Cheese(models.Model):
  brand = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return f'{self.brand} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'cheese_id': self.id})