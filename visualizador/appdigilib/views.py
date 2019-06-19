from django.shortcuts import render
from django.shortcuts import redirect
import urllib3
import json as JSON
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.views.decorators.csrf import requires_csrf_token
from django.http import JsonResponse, HttpResponse
from .forms import *
from django.db.models import Q
from django.template import RequestContext
from appdigilib.models import Articulo, Categoria, AnaliticTask, Image
from appdigilib.forms import ArticleForm, CategoriaForm, AnaliticTaskForm


#   Metodo para renderizar la pagina principal:
#   Entrada: @categoria, @tareas_analiticas, @articulos
#   @Comprueba cuales son los articulos que hay que mostrar dependiento de las selecciones hecha en la vista
#   Devuelve: @lista de articulos
@requires_csrf_token
def listado(request = None, articulos = None):

    #se method e' post e' porque e' chamado da busqueda
    if request.method == 'POST':
        string_search = request.POST.get('search')   #El texto que tengo que buscar
        #Consulta para buscar por el titulo, autor y Resumen
        # da error con esta busqueda... | Q(text__contains=string_search) ....debe ser por el tipo de dato en models
        articulos = Articulo.objects.filter(Q(title__contains=string_search) | Q(autor__contains=string_search ))
    else:
                         #Extrae las imagenes de los articulos
        articulos = Articulo.objects.all().order_by('published_date')       #Extrae los articulos
    categorias = Categoria.objects.all()                                #Extrae todas las cateorias insertadas
    tareas = AnaliticTask.objects.all()                                 #EXtrae todas las tareas analiticas insertadas
    imagenes = Image.objects.all().order_by('articulo')

    return render(request, 'list/index_list.html',
                  {'articulos': articulos, 'categorias': categorias, 'tareas': tareas, 'imagenes': imagenes})



#   Metodo para actualizar los articulos dependiento de las categoria marcadas en la vista:
#   Entrada: @peticion Ajax de la vista
#   @Comprueba para cada articulo, si la tiene la categoria desmarcada y si solo tiene esa categoria, lo quita
#   de la lista de articulos a mostrar
@requires_csrf_token
def actualizar_articuloXcategoria(request):

    #Compruebo si viene por el POST
    if request.method == 'POST':
        #Guardo la lista de categorias que envio el Ajax
        categoria_marcada = request.POST.getlist('lista[]')
        print(categoria_marcada)


        todos_art = []  #Para almacenar los articulos que voy a mostrar
        articulos_mostrar = list(Articulo.objects.all().prefetch_related('categorias'))
        #print(articulos_mostrar)

        #Para cada articulo compruebo si tiene al menos una categoria marcada, lo adiciono en @todos_art
        for x in range(0,len(articulos_mostrar)):
            for y in range(0,len(categoria_marcada)):
                if( CateSerach(articulos_mostrar[x], categoria_marcada[y])):
                    todos_art.append(articulos_mostrar[x])
                    break
            #if cont != 0:
            #    todos_art.append(articulos_mostrar[x])

    else:
        todos_art = Articulo.objects.all().values(Articulo.title, Articulo.autor)

    html = render_to_string('list/render.html', {'articulos': todos_art})
    return HttpResponse(html)



@requires_csrf_token
def actualizar_articuloXtask(request):

    categorias = Categoria.objects.all()
    tareas = AnaliticTask.objects.all()
    articulos = Articulo.objects.all().order_by('image__articulo__published_date')
    imagenes = Image.objects.all().order_by('articulo')

    return render(request, 'list/index_list.html',
                {'articulos': articulos, 'categorias': categorias, 'tareas': tareas, 'imagenes': imagenes})



#Metodo auxiliar que busca si un articulo tiene una determinada categorìa
# Entrada:@un articulo, @una categoria
#Devuelve True si ese articulo tiene esa categoria, False en caso contrario
def CateSerach(sarticulo, scategoria):

    #buscar_categoria= Categoria(scategoria) #La categoria que voy a buscar en la lista que tiene el articulo
    list_cat_art = list(sarticulo.categorias.all())     #Todas las categorias del articulo
    #Para cada categoria del articulo si es igual a la entrada
    for c in range(0,len(list_cat_art)):
        if(list_cat_art[c].categoria == scategoria):
          return True
    return False


#Metodo auxiliar que busca si un articulo tiene una determinada tarea analitica
# Entrada:@un articulo, @una tarea
#Devuelve True si ese articulo tiene esa tarea, False en caso contrario
def TaskSearch(sarticulo, stask):

    busca_task = AnaliticTask(stask)    #La tarea que voy a buscar en el articulo
    list_task_art = list(sarticulo.task.all())      #Lista de tareas del acrticulo

    #Para cada tarea del articulo si es igual a la entrada
    for t in list_task_art:
        if t== busca_task:
            return True
    return False


#Metodo para busca articulos, dando una frase
#Entrada:@ texto
#Devuelve: @Lista de articulos que contienen el texto en el Titulo, Autor o Resumen
def Search(request):

    string_search = request.POST.get('search')   #El texto que tengo que buscar
    print(string_search)
    #Consulta para buscar por el titulo, autor y Resumen
    # da error con esta busqueda... | Q(text__contains=string_search) ....debe ser por el tipo de dato en models
    articles_names = Articulo.objects.filter(Q(title__contains=string_search) | Q(autor__contains=string_search ))

    #html = render_to_string('list/render.html', {'articulos': articles_names})
    #return HttpResponse(html)
    return listado(request, articles_names)





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