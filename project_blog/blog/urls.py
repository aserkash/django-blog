from django.urls import path
from . import views #import views from app 'blog'

urlpatterns = [
    path('', views.home, name ='blog-home'),
    path('about/', views.about, name = 'blog-about'),
]