from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name='about'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('basket', views.basket, name='basket'),
    path('opinions', views.opinions, name='opinions'),

]