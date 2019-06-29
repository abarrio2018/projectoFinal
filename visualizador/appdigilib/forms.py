"""
Create by abarrio
Date: 08/04/2019
"""


from django import forms
from .models import Article, Category, AnaliticTask, Image


#Form for the model of the article
class ArticleForm(forms.ModelForm):
    class Meta:
       model = Article
       fields = [
                'title', 'categories', 'tasks', 'doi',
                'author', 'published_date', 'text',
                ]
       labels = {
                'title': 'Tìtulo',
                'categories':'Categoría',
                'tasks':'Tarefa analìtica' ,
                'doi':'DOI',
                'author': 'Ator',
                'published_date': 'Data de publicação',
                'text': 'Texto'
                }
       widgets = {
                'title': forms.TextInput,
                'category':forms.Select,
                'task':forms.Select,
                'doi':forms.TextInput,
                'author':forms.TextInput,
                'published_date':forms.TextInput,
                'text': forms.TextInput,
                }


#Form for the model of the category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category',)
        widgets = {'category': forms.Select,}


#Form for the model of the analytical task
class AnaliticTaskForm(forms.ModelForm):
    class Meta:
        model = AnaliticTask
        fields = ('task',)
        widgets = {'task': forms.Select, }


#Form for the model of the imagen
class ImagenForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
