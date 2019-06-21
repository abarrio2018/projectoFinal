from django import forms
from .models import Article, Category, AnaliticTask, Image


class ArticleForm(forms.ModelForm):
    class Meta:
       model = Article
       fields = ['title', 'categories', 'tasks', 'doi', 'author', 'published_date', 'text',]
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

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category',)
        widgets = {'category': forms.Select,}

class AnaliticTaskForm(forms.ModelForm):
    class Meta:
        model = AnaliticTask
        fields = ('task',)
        widgets = {'task': forms.Select, }

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
