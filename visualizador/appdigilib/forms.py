from django import forms
from .models import Articulo, AnaliticTask, Categoria

class ArticleForm(forms.ModelForm):
    class Meta:
       model = Articulo
       fields = ('title', 'categoria', 'task', 'doi', 'autor', 'published_date', 'text')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('categoria')

class AnaliticTaskForm(forms.ModelForm):
    class Meta:
        model = AnaliticTask
        fields = ('task')
