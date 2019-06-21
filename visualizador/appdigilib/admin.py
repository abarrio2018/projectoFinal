from django.contrib import admin
from .models import Article, Category, AnaliticTask, Image
# Register your models here.


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(AnaliticTask)
admin.site.register(Image)
