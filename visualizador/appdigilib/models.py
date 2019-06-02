from statistics import mode
from xmlrpc.client import DateTime

from django.db import models
from django.utils.timezone import now
from datetime import date
# Create your models here.

class Categoria(models.Model):
    categoria= models.CharField(max_length=200)

    def __str__(self):
       return self.categoria

class AnaliticTask(models.Model):
    task = models.CharField(max_length=250)

    def __str__(self):
        return self.task

class Articulo(models.Model):
    autor = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    doi = models.CharField(max_length=250)
    text = models.TextField()
    published_date = models.DateField()
    categoria = models.ManyToManyField(Categoria)
    task = models.ManyToManyField(AnaliticTask)
    # autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#    categorias = (
#   ('Select', 'select'), ('Correlation', 'correlations'), ('Ranking', 'ranking'), ('Part of whole', 'part_Whole'),
#    ('Evolution', 'evolution'))
#    categoria = models.CharField(max_length=50, choices=categorias, default= 'Select')
#    tasks = (('Labeled','Etiquetado'), ('Clustering','Agrupago'), ('Hightligth', 'Resaltado'),('Sumary', 'Resumido'))
#   task = models.CharField(max_length=50, choices= tasks, default='Labeled')


    def only_year(self):
        return self.timestamp.strftime('%Y')

    def StrArticulo(self):
        cadena= "{1},{0}"
        return cadena.format(self.title, self.autor)

    def __str__(self):
        return self.StrArticulo()