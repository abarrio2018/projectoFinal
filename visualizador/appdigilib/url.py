from django.urls import path
from appdigilib.views import *
from appdigilib import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.listado, name='post_list'),
    path('Imagem/nova', AdicionarImagen, name ='nova_img'),
    path('index/c1',views.actualizar_articuloXcategoria, name='list_cat'),
    path('index/c2', views.actualizar_articuloXtask, name='list_task'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)