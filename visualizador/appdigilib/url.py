"""
Create by abarrio
Date: 08/04/2019
"""
from django.urls import path
from appdigilib.views import *
from appdigilib import views
from django.conf import settings
from django.conf.urls.static import static


#My own route file
urlpatterns = [

    path('', views.show_list, name ='post_list'),
    path('Imagem/nova', views.add_image, name ='nova_img'),
    path('index/c1', views.update_article_category, name ='list_cat'),
    path('index/c2', views.update_article_task, name ='list_task'),
    path('search/', views.search, name ='buscar'),
    path('detail/', views.details, name ='detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)