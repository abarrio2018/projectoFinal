from django.urls import path
from .views import listado

urlpatterns = [

    path('', listado, name ='index_list'),
]