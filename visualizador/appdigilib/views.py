from django.shortcuts import render
from django.shortcuts import redirect
import urllib3
import PIL.Image
import json as JSON
from django.views.generic import ListView
from django.http import JsonResponse


from .forms import *
from appdigilib.models import Articulo, Categoria, AnaliticTask, Image
from appdigilib.forms import ArticleForm, CategoriaForm, AnaliticTaskForm

# Create your views here.


def listado(request):
    categorias = Categoria.objects.all()
    tareas = AnaliticTask.objects.all()
    articulos = Articulo.objects.all().order_by('image__articulo__published_date')
    #file = request.FILES
#    imag = PIL.Image.open('images/index.jpeg')
#    imag.load()
#    imag.split()

    return render(request, 'list/index_list.html', {'articulos': articulos, 'categorias': categorias, 'tareas': tareas})


#Insertar con formulario
class Article():

    def AdicionarArticulo(request):
        if request.method == 'post':
            form = ArticleForm(request.POST)

            if form.is_valid():
                form.save(commit=True)
                return redirect('add_article', pk=post.pk)
        else:
            form = ArticleForm
        return render(request, 'list/article.html', {'form': form})

