from django.contrib import admin
from .models import Article, Category, AnaliticTask, Image, DataSource

#Using the administrator application to insert data
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(AnaliticTask)
admin.site.register(Image)
admin.site.register(DataSource)
