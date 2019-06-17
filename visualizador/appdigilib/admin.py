from django.contrib import admin
from .models import Articulo, Categoria, AnaliticTask, Image, Articulo_Categoria, Articulo_Task
# Register your models here.


admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(AnaliticTask)
admin.site.register(Articulo_Categoria)
admin.site.register(Articulo_Task)
admin.site.register(Image)
