from django.shortcuts import render
from django.shortcuts import redirect
import urllib3
import json as JSON
from django.http import JsonResponse
from appdigilib.models import Articulo, Categoria
from appdigilib.forms import ArticleForm, CategoriaForm, AnaliticTaskForm

# Create your views here.
def index_list(request):
    http = urllib3.PoolManager()

    #json = JSON.loads(response)
    json = request.data
    return render(request, 'list/index_list.html', {'titulo': json})

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
