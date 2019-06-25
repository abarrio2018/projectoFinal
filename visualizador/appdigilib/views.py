from django.shortcuts import render, redirect
import json as JSON
from django.core import serializers
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.views.decorators.csrf import requires_csrf_token
from django.http import JsonResponse, HttpResponse
import simplejson
from django.http import QueryDict
from .forms import *
import datetime
from django.db.models import Q
from django.template import RequestContext
from appdigilib.models import Article, Category, AnaliticTask, Image
from appdigilib.forms import ArticleForm, CategoryForm, AnaliticTaskForm


"""Metodo para renderizar la pagina principal:
   Entrada: @categoria, @tareas_analiticas, @articulos
   Comprueba cuales son los articulos que hay que mostrar dependiento de las selecciones hecha en la vista
   Devuelve: @lista de articulos
"""
@requires_csrf_token
def List(request):

    if request.method == 'POST':                                                #Comprueba si el metodo el POST, viene de la busqueda
        string_search = request.POST.get('search')                              #El texto que tengo que buscar

        #Consulta para buscar por el titulo, autor y Resumen
        articles = Article.objects.filter(Q(title__contains = string_search) | Q(author__contains = string_search))

    else:
        articles = Article.objects.all().order_by('published_date')             #Extrae todos los articulos
    categories = Category.objects.all()                                         #Extrae todas las cateorias insertadas
    tasks = AnaliticTask.objects.all()                                          #EXtrae todas las tareas analiticas insertadas
    images = Image.objects.all().order_by('article')                            #Extrae las imagenes de los articulos



    return render(request, 'list/index_list.html',
                  {'articles': articles, 'categories': categories, 'tasks': tasks, 'images': images})


"""Metodo para actualizar los articulos dependiendo de las categoria marcadas en la vista:
   Entrada: @peticion Ajax de la vista con los check marcados.
   Comprueba para cada articulo, si tiene al menos una categoria de la lista, sino, lo quita
   de la lista de articulos a mostrar
   Salida: La lista de articulos a mostrar
"""
@requires_csrf_token
def Update_ArticleXCategory(request):

    if request.method == 'POST':                                                            #Compruebo si la peticion es segura
        check_category = request.POST.getlist('lista[]')                                    #Guardo la lista de categorias que enviò la peticiòn

        all_articles = []                                                                    #Para almacenar los articulos que voy a mostrar
        articles_mostrar = list(Article.objects.all().prefetch_related('categories'))

        #Para cada articulo compruebo si tiene al menos una categoria marcada, lo adiciono en @all_articles
        for x in range(0, len(articles_mostrar)):
            for y in range(0, len(check_category)):

                if Serach_Category(articles_mostrar[x], check_category[y]):                #Metodo auxiliar que dice si una categoria esta en un articulo
                    all_articles.append(articles_mostrar[x])
                    break
    else:
        all_articles = Article.objects.all().values(Article.title, Article.author)

    html = render_to_string('list/render.html', {'articles': all_articles})
    return HttpResponse(html)


"""Metodo para actualizar los articulos dependiendo de las tareas analiticas marcadas en la vista:
   Entrada: @peticion Ajax de la vista con los check marcados.
   Comprueba para cada articulo, si tiene al menos una tarea analitica de la lista, sino, lo quita
   de la lista de articulos a mostrar
   Salida: La lista de articulos a mostrar
"""
@requires_csrf_token
def Update_ArticleXTask(request):

    if request.method == 'POST':                                                            #Compruebo si la peticion es segura
        task_marcada = request.POST.getlist('lista[]')                                      #Guardo la lista de tareas que enviò la peticiòn

        all_articles = []                                                                   #Para almacenar los articulos que voy a mostrar
        articles_mostrar = list(Article.objects.all().prefetch_related('tasks'))            #Total de articulos actuales

        #Para cada articulo compruebo si tiene al menos una tarea marcada, lo adiciono en @all_articles
        for x in range(0, len(articles_mostrar)):
            for y in range(0, len(task_marcada)):

                if Search_Task(articles_mostrar[x], task_marcada[y]):                     #Metodo auxiliar que dice si una categoria esta en un articulo
                    all_articles.append(articles_mostrar[x])
                    break
    else:
        all_articles = Article.objects.all().values(Article.title, Article.author)

    html = render_to_string('list/render.html', {'articles': all_articles})
    return HttpResponse(html)


"""Metodo auxiliar que busca si un articulo tiene una determinada categorìa
    Entrada:@un articulo, @una categoria
    Devuelve True si ese articulo tiene esa categoria, False en caso contrario"""
def Serach_Category(sarticle, scategory):

    list_cat_art = list(sarticle.categories.all())                 #Todas las categorias del articulo que viene como entrada


    for c in range(0, len(list_cat_art)):                            #Para cada categoria del articulo si es igual a la categoria entrada
        if list_cat_art[c].category == scategory:
          return True
    return False


"""Metodo auxiliar que busca si un articulo tiene una determinada tarea analitica
    Entrada:@un articulo, @una tarea
    Devuelve True si ese articulo tiene esa tarea, False en caso contrario"""


def Search_Task(sArticle, stask):

    list_task_art = list(sArticle.tasks.all())                          #Lista de tareas del acrticulo de entrada

    for t in range(0,len(list_task_art)):                               #Busca la tarea de la entrada en cada una de las que tiene el articulo
        if list_task_art[t].task == stask:
            return True
    return False


"""Metodo para busca articulos, dando una frase
    Entrada:@texto
    Devuelve: @Lista de articulos que contienen el texto en el Titulo, Autor o Resumen
"""


def Search(request):

    string_search = request.POST.get('search')                                           #El text que tengo que buscar

    articles_names = Article.objects.filter(Q(title__contains=string_search) |          #Consulta para buscar por el titulo, autor y Resumen
                                             Q(author__contains=string_search |
                                             Q(text__contains=string_search)))

    #Consulta para buscar por el titulo, autor y Resumen
    # da error con esta busqueda... | Q(text__contains=string_search) ....debe ser por el tipo de dato en models
    articles_names = Article.objects.filter(Q(title__contains=string_search) | Q(author__contains=string_search))

    html = render_to_string('list/render.html', {'articles': articles_names})
    return HttpResponse(html)                                                           #Devuelve el HTML con los articulos


"""Metodo para visualizar los detalles del articulo
    Entrada: un articulo seleccionado
    Salida: Todos los datos del articulo en un html para ser mostrados
"""
def Details(request):

    if request.method == 'POST':                                             #Compruebo si la peticion es segura

        id = request.POST.get('id_article')

        date_article = Article.objects.get(pk = id)                         #Obtener el objeto del art[iculo
        categories = date_article.categories.all().only('category')         #Pido el objeto de tipo categoria del articulo
        categories = list(categories.values('category'))                    #Para manejar la categoria la convierto en diccionario
        task = date_article.tasks.all().only('task')                        #Pido el objeto de tipo categoria del articulo
        task = list(task.values('task'))                                    #Para manejar la tarea la convierto en diccionario

        title = date_article.title
        author = date_article.author
        year = date_article.published_date
        doi = date_article.doi
        images = date_article.image

    return render(request, 'list/modal.html',                               #Mando a crear el cuerpo del modal con los respectivos datos
                  {'categories': categories, 'year': year, 'doi':doi,
                   'task': task, 'images': images,
                   'title': title, 'author': author
                   })


def Add_Image(request):
    categories = Category.objects.all()
    tasks = AnaliticTask.objects.all()

    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return redirect('post_list')
        else:
            return redirect('error')
    else:
        form = ImagenForm
    return render(request, 'list/article.html', {'form': form, 'categories': categories, 'tasks': tasks})

"""
Método auxiliar para extraer solo el año de la fecha
Entrada:
Salida: 
"""
def FormarYear(date):
    print(date)
    #str(date)
    year = date.year
    print(year)

    #format_year= year.strftime('%y')
    #print (format_year)

    return year


def error(request):
    return HttpResponse("Algo deu errado.")