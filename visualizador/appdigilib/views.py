from django.shortcuts import render
from django.shortcuts import redirect
import urllib3
import json as JSON
from django.views.generic import ListView
from django.http import JsonResponse
from .forms import *
from django.template import RequestContext
from appdigilib.models import Articulo, Categoria, AnaliticTask, Image
from appdigilib.forms import ArticleForm, CategoriaForm, AnaliticTaskForm

# Create your views here.


def listado(request):
    categorias = Categoria.objects.all()
    tareas = AnaliticTask.objects.all()
    articulos = Articulo.objects.all().order_by('image__articulo__published_date')
    imagenes= Image.objects.all().order_by('articulo')
    #file = request.FILES
    #imag = PIL.Image.open('images/index.jpeg')
#    imag.load()
#    imag.split()

    return render(request, 'list/index_list.html', {'articulos': articulos, 'categorias': categorias, 'tareas': tareas, 'imagenes':imagenes})


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


#Insertar con formulario
def AdicionarImagen(request):
    categorias = Categoria.objects.all()
    tareas = AnaliticTask.objects.all()

    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return redirect('post_list')
        else:
            return redirect('error')
    else:
        form = ImagenForm
    return render(request, 'list/article.html', {'form': form, 'categorias': categorias, 'tareas': tareas})


def error(self):
    return ('Arquivo com problema')