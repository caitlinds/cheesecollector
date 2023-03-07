from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cheeses/', views.cheeses_index, name='index'),
  path('cheeses/<int:cheese_id>/', views.cheeses_detail, name='detail'),
  path('cheeses/create/', views.CheeseCreate.as_view(), name='cheeses_create')
]