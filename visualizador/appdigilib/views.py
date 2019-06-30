"""
Create by abarrio
Date: 08/04/2019
"""
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


""" Method to render the main page:
    Input: @request
    Check which items are to be shown depending on the selections made in the view
    Returns: @list of articles
"""
@requires_csrf_token
def show_list(request):
    if request.method == 'POST':                                        # Check if the POST method comes from the search
        string_search = request.POST.get('search')                      # I save the text to search

        articles = Article.objects.filter(                              # Query to search by title and author
            Q(title__contains=string_search) |
            Q(author__contains=string_search)
        )
    else:
        articles = Article.objects.all().order_by('published_date')     # Show all articles without having searched

    categories = Category.objects.all()                                 # Save all categories for left menu
    tasks = AnaliticTask.objects.all()                                  # Save all analytical tasks for left menu
    images = Image.objects.all().order_by('article')                    # Save all the images of the articles

    return render(request, 'list/index_list.html',
                  {'articles': articles,                                # List the items in the main interface
                   'categories': categories,                            # load all the data from the left menu
                   'tasks': tasks,
                   'images': images}
                  )


"""Method to update the articles depending on the category marked in the view:
    Input: Ajax @peticion of the view with the check marked.
    Check for each item, if it has at least one category of the list, else, 
    remove it from the list of items to display.
    Returns: The list of items to be displayed
"""
@requires_csrf_token
def update_article_category(request):

    if request.method == 'POST':                                                            #I check if the request is safe
        check_category = request.POST.getlist('lista[]')                                    #I save the list of categories that sent the request
        all_articles = []                                                                   #will store the items that I will show
        articles_show = list(Article.objects.all().prefetch_related('categories'))          #Total of current articles

        #I check if the article has at least one of the categories that are marked,
        # I add it in @all_articles
        for x in range(0, len(articles_show)):
            for y in range(0, len(check_category)):

                # Auxiliary method that says if a category is in an article
                if serach_category(articles_show[x], check_category[y]):
                    all_articles.append(articles_show[x])
                    break
    else:
        all_articles = Article.objects.all().values(Article.title, Article.author)

    html = render_to_string('list/render.html', {'articles': all_articles})
    return HttpResponse(html)


"""Method to update the articles depending on the analytical tasks marked in the view:
    Input: Ajax @peticion of the view with the check marked.
    Check for each item, if it has at least one analytical task from the list, else, 
    remove it from the list of items to display
    Return: The list of items to be displayed
"""
@requires_csrf_token
def update_article_task(request):

    if request.method == 'POST':                                                            #I check if the request is safe
        task_checked = request.POST.getlist('lista[]')                                      #I save the list of Task that sent the request

        all_articles = []                                                                   #will store the items that I will show
        articles_show = list(Article.objects.all().prefetch_related('tasks'))               #Total of current articles

        #For each article I check if it has at least one task marked,
        # I add it in @all_articles
        for x in range(0, len(articles_show)):
            for y in range(0, len(task_checked)):

                if search_task(articles_show[x], task_checked[y]):                     #Auxiliary method that says if a task is in an article
                    all_articles.append(articles_show[x])
                    break
    else:
        all_articles = Article.objects.all().values(Article.title, Article.author)

    html = render_to_string('list/render.html', {'articles': all_articles})
    return HttpResponse(html)


"""Auxiliary method that searches if an article has a certain category.
     Input: @a article, @a category
     Returns True if that item has this category, False otherwise.
"""
def serach_category(s_article, s_category):

    list_cat_art = list(s_article.categories.all())             #All categories of the article that comes as an entry


    for c in range(0, len(list_cat_art)):                      #Search if the entry category exists in the article
        if list_cat_art[c].category == s_category:
          return True
    return False


"""Auxiliary method that searches if an article has a certain analytical task.
     Input: @an article, @a task
     Returns True if that article has that task, False otherwise
"""
def search_task(s_article, s_task):

    list_task_art = list(s_article.tasks.all())                   #Task list of the input article

    for t in range(0,len(list_task_art)):                         #Search if the task exists in the article
        if list_task_art[t].task == s_task:
            return True
    return False


"""Method to search for articles, giving a phrase
    Input: @text
    Returns: @ List of articles that contain the text in the Title or Author
"""
@requires_csrf_token
def search(request):

    string_search = request.POST.get('search')                                          #The text that I have to search

    articles_names = Article.objects.filter(Q(title__contains=string_search) |          #Query to search by title, author and Summary
                                             Q(author__contains=string_search |
                                             Q(text__contains=string_search)))

    html = render_to_string('list/render.html', {'articles': articles_names})
    return HttpResponse(html)                                                           #Returns the found articles


"""Method to visualize the details of the article
     Input: a selected article
     Return: All the data of the article in an html to be shown
"""
def details(request):
    if request.method == 'POST':                                             #If the details were requested
        id = request.POST.get('id_article')

        data_article = Article.objects.get(pk = id)                         #I get the object of the article
        categories = data_article.categories.all().only('category')         #I get the Category of the article as an object
        categories = list(categories.values('category'))                    #To the Category object, I ask for the values
        task = data_article.tasks.all().only('task')                        #I get the tasks of the article as an object
        task = list(task.values('task'))                                    #To the Task object, I ask for the values

        title = data_article.title
        author = data_article.author
        year = data_article.published_date
        doi = data_article.doi
        images = data_article.image

    return render(request, 'list/modal.html',                               #Create the body of the modal with the respective data
                  {'categories': categories, 'year': year, 'doi':doi,
                   'task': task, 'images': images,
                   'title': title, 'author': author
                   })


"""Method to insert an image in my static directory"""
def add_image(request):
    categories = Category.objects.all()                         #Save all categories for left menu
    tasks = AnaliticTask.objects.all()                          #Save all task for left menu

    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)          #Form with the files

        if form.is_valid():
            form.save(commit=True)
            return redirect('post_list')                        #Show the initial page after saving the form
        else:
            return redirect('error')                            #The form is not valid
    else:
        form = ImagenForm
    return render(request, 'list/article.html',
                  {'form': form,
                   'categories': categories,
                   'tasks': tasks}
                  )


"""Auxiliary method that shows a standard error"""
def error(request):
    return HttpResponse("Something is wrong.")