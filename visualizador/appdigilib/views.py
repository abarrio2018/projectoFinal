from django.shortcuts import render
from django.shortcuts import redirect
import urllib3
import json as JSON
from django.template.loader import render_to_string
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
    #Peticion para todo en la base de dato
    categorias = Categoria.objects.all()
    tareas = AnaliticTask.objects.all()
    imagenes = Image.objects.all().order_by('articulo')
    articulos = Articulo.objects.all().order_by('published_date')
    return render(request, 'list/index_list.html',
                  {'articulos': articulos, 'categorias': categorias, 'tareas': tareas, 'imagenes': imagenes})


#   Metodo para actualizar los articulos dependiento de las categoria marcadas en la vista:
#   Entrada: @peticion Ajax de la vista
#   @Comprueba para cada articulo, si la tiene la categoria desmarcada y si solo es esa, lo quita
#   de la lista de articulos a mostrar
@requires_csrf_token
def actualizar_articuloXcategoria(request):

    if request.method == 'POST':
        categoria_desmarcada = request.POST.get('lista_c[]')
        print(categoria_desmarcada)


        todos_articulos = Articulo.objects.all()
        print(categoria_desmarcada)
        #print(categoria_marcada)

        art_activo = []
        for articulo in todos_articulos:
            tus_categoria = articulo.categoria.filter(articulo__categoria__articulo=True)

            print(tus_categoria)
            if CateSerach(articulo, categoria_desmarcada):
                articulo.categoria.activo = False
                print("Paso2 "+categoria_desmarcada)

            if tus_categoria.count() != 0:
                art_activo += articulo
    else:
        print("Paso3")
        art_activo = Articulo.objects.all().values(Articulo.title, Articulo.autor)
        html = render_to_string('list/render.html', {'articulos': art_activo})
        return HttpResponse(html)

    #json_data = JSON.dumps(art_activo, ensure_ascii= False)
    #return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(dict(list(art_activo)))

@requires_csrf_token
def actualizar_articuloXtask(request):

    categorias = Categoria.objects.all()
    tareas = AnaliticTask.objects.all()
    articulos = Articulo.objects.all().order_by('image__articulo__published_date')
    imagenes = Image.objects.all().order_by('articulo')

    return render(request, 'list/index_list.html',
                {'articulos': articulos, 'categorias': categorias, 'tareas': tareas, 'imagenes': imagenes})


#Comprobar articulos
def Lista_Articulo(categoria, articulos_actuales):
    articulos_actuales = Articulo(articulos_actuales)
    categoria_eliminada = Categoria(categoria)

    for a in articulos_actuales:
        if((CateSerach(a,categoria_eliminada)) & (CantCategorias(a)==1)):
            articulos_actuales = articulos_actuales.delete(a)

    return articulos_actuales


#Busca si un articulo tiene una determinada categorìa
def CateSerach(sarticulo, scategoria):
    #myarticulo= Articulo(sarticulo)
    buscar_categoria= Categoria(scategoria)
    list_cat_art = sarticulo.categoria.all()

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


def error(request):
    return HttpResponse("Algo deu errado")