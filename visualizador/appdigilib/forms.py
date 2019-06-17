from django import forms
from .models import Articulo, Categoria, AnaliticTask, Image, Articulo_Task, Articulo_Categoria

class ArticleForm(forms.ModelForm):
    class Meta:
       model = Articulo
       fields = ['title', 'categorias', 'tasks', 'doi', 'autor', 'published_date', 'text',]
       labels = {
           'title': 'Tìtulo',
           'categorias':'Categoría',
           'tasks':'Tarefa analìtica' ,
           'doi':'DOI',
           'autor': 'Ator',
           'published_date': 'Data de publicação',
           'text': 'Texto'
       }
       widgets = {
           'title': forms.TextInput,
           'categoria':forms.Select,
           'task':forms.Select,
           'doi':forms.TextInput,
           'autor':forms.TextInput,
           'published_date':forms.TextInput,
           'text': forms.TextInput,
       }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('categoria',)
        widgets = {'categoria': forms.Select,}

class AnaliticTaskForm(forms.ModelForm):
    class Meta:
        model = AnaliticTask
        fields = ('task',)
        widgets = {'task': forms.Select, }

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
