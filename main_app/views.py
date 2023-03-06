from django.shortcuts import render
from .models import Cheese

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cheeses_index(request):
  cheeses = Cheese.objects.all()
  return render(request, 'cheeses/index.html', {
    'cheeses': cheeses
  })