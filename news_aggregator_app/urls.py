from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.listAndSearchNews, name='news'),
    path('news/favourite', views.favouriteNews, name='news'),

]