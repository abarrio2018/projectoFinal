from django.urls import path
from appdigilib.views import *
from appdigilib import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('Imagem/nova', AdicionarImagen, name ='nova_img'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)