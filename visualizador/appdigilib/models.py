from statistics import mode
from xmlrpc.client import DateTime
from django.db import models
from django.utils.timezone import now
from datetime import date
# Create your models here.

class Categoria(models.Model):
    categoria= models.CharField(max_length=250)
    activo = models.BooleanField()

    def __str__(self):
       return self.categoria

class AnaliticTask(models.Model):
    task = models.CharField(max_length=250)

    def __str__(self):
        return self.task

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.image)

class Articulo(models.Model):
    autor = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    doi = models.CharField(max_length=250)
    text = models.TextField()
    published_date = models.DateField()
    categoria = models.ManyToManyField(Categoria)
    task = models.ManyToManyField(AnaliticTask)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def only_year(self):
        return self.timestamp.strftime('%Y')

    def StrArticulo(self):
        cadena = "{1},{0}"
        return cadena.format(self.title, self.autor)

    def __str__(self):
        return self.StrArticulo()