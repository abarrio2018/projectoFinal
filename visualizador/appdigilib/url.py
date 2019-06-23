from django.urls import path
from appdigilib.views import *
from appdigilib import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.List, name ='post_list'),
    path('Imagem/nova', views.Add_Image, name ='nova_img'),
    path('index/c1', views.Update_ArticleXCategory, name ='list_cat'),
    path('index/c2', views.Update_ArticleXTask, name ='list_task'),
    path('search/', views.Search, name ='buscar'),
    path('detail/', views.Details, name ='detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)