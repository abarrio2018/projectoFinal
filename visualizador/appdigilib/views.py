from django.shortcuts import render
from django.shortcuts import redirect
import urllib3
import json as JSON
from django.http import JsonResponse
from . models import Articulo, AnaliticTask, Categoria
from .forms import ArticleForm, AnaliticTask, Categoria

# Create your views here.
def index_list(request):
    http = urllib3.PoolManager()
    #response = http.request('GET', 'http://ieeexploreapi.ieee.org/api/v1/search/articles?apikey=nssztavfsrz2b9d2ftwmxqxk&format=json&max_records=25&start_record=1&sort_order=asc&sort_field=article_number&article_title=visualization')
    response = http.request('GET', 'http://api.springernature.com/metadata/json/doi/10.1007/s00766-013-0194-3?api_key=2fa1f8821acc31bf10c043665bafa902')
    #json = JSON.loads(response)
    json = response.data
    return render(request, 'list/index_list.html', {'titulo': json})

###Insertar manualmente
def insertArticle(request):
    json = JSON.loads(request.body)

    articulo = Articulo(**json)
    articulo.save()

    return JsonResponse({"msj": "Se ha adicionado el artìculo satisfactoriamente"})

#Insertar con formulario
def addArticle(request):

    if request.method == 'post':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('add_article', pk=post.pk)
    else:
        form = ArticleForm
    return render(request, 'list/article.html', {'form': form})