from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-loadout', views.create_loadout, name='create-loadout'),
]