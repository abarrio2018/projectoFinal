from django.shortcuts import render
from django.shortcuts import redirect
import urllib3
import json as JSON
from django.views.generic import ListView
from django.views.decorators.csrf import requires_csrf_token
from django.http import JsonResponse, HttpResponse
from .forms import *
from django.template import RequestContext
from appdigilib.models import Articulo, Categoria, AnaliticTask, Image
from appdigilib.forms import ArticleForm, CategoriaForm, AnaliticTaskForm


#   Metodo para renderizar la pagina principal:
#   Entrada: @categoria, @tareas_analiticas, @articulos
#   @Comprueba cuales son los articulos que hay que mostrar dependiento de las selecciones en la vista
@requires_csrf_token
def listado(request):

    #Peticion para recuperar toda las categorias y las tareas del banco. Ellas siempre se muestran en menu izquierdo
    categorias = Categoria.objects.all()
    tareas = AnaliticTask.objects.all()

    #Peticion al la funcionalidad Actualizar articulo, para comproobar si se puede mostrar este articulo
    articulos = actualizar_articuloXcategoria(request)

    #Hacer un DISTINT para actualizar los articulos dependiendo tambien las tareas

    #Peticion para buscar las imagenes de los articulos
    imagenes = Image.objects.all().order_by('articulo')

    return render(request, 'list/index_list.html',
                  {'articulos': articulos, 'categorias': categorias, 'tareas': tareas, 'imagenes': imagenes})


#  Metodo para actualizar los articulos que van a mostrarse dependiento de las categoria marcadas en la vista:
#   Entrada: @peticion Ajax de la vista
#   Comprueba para cada articulo, si la tiene la categoria desmarcada y si solo es esa, lo quita
#   de la lista de articulos a mostrar
@requires_csrf_token
def actualizar_articuloXcategoria(request):

    if request.method == 'POST':
        categoria_desmarcada = request.POST
        art_activo = []
        print("Paso1 "+categoria_desmarcada)

        #Para cada articulo en BD
        for articulo in Articulo.objects.all():

            #Guardo sus categorias activas
            tus_categoria = articulo.categoria.filter(activo=True)

            # Para cada categoria desmarcada
            for des_cat in categoria_desmarcada:

                #Pregunto si la categoria esta en el articulo para desmarcarla
                if CateSerach(articulo, des_cat):
                    articulo.categoria.activo = False
                    print("Paso2 "+des_cat)

            # Compruebo si no le quedan categorias marcadas
            if tus_categoria.count() != 0:
                art_activo += articulo
    else:
        #Si no vienes por el POST, cargo todos los articulos almacenados
        print("Paso3")
        art_activo = Articulo.objects.all().order_by('image__articulo__published_date')

    #Devuelvo los articulos que tienen categorias activas
    return art_activo

@requires_csrf_token
def actualizar_articuloXtask(request):

    categorias = Categoria.objects.all()
    tareas = AnaliticTask.objects.all()
    articulos = Articulo.objects.all().order_by('image__articulo__published_date')
    imagenes = Image.objects.all().order_by('articulo')

    return render(request, 'list/index_list.html',
                {'articulos': articulos, 'categorias': categorias, 'tareas': tareas, 'imagenes': imagenes})




#Busca si un articulo tiene una determinada categorìa
def CateSerach(sarticulo, scategoria):
    myarticulo= Articulo(sarticulo)
    buscar_categoria= Categoria(scategoria)
    list_cat_art = myarticulo.categoria.all()

    for c in list_cat_art:
        if(c == buscar_categoria):
          return True
    return False

#Busca si un artìculo tiene determinada tarea analìtica
def TaskSearch(sarticulo, stask):
    myarticulo = Articulo(sarticulo)
    busca_task = AnaliticTask(stask)
    list_task_art = myarticulo.task.all()

    for t in list_task_art:
        if t== busca_task:
            return True
    return False


#Contar categoria de un articulo determinado
def CantCategorias(articulo):
    myarticulo= Articulo(articulo)
    return myarticulo.categoria.all().count()


#Contar tareas analitica de un articulo determinado
def CantTareas(articulo):
    myarticulo = Articulo(articulo)
    return myarticulo.task.all().count()


#Insertar articulo con formulario
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


#Insertar imagen con formulario
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


def error(request):
    return HttpResponse("Algo deu errado")

def Search():
    #usuarios = Usuarios.objects.filter(nome__icontains='Jonh')
    return HttpResponse("Estas buscando que?")

