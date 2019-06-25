from statistics import mode
from xmlrpc.client import DateTime
from django.db import models
from django.utils.timezone import now
from datetime import date
from django.core.validators import MinValueValidator
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
       return self.category


class AnaliticTask(models.Model):
    task = models.CharField(max_length=250)

    def __str__(self):
        return self.task


class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.image)


class Article(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    doi = models.CharField(max_length=250)
    text = models.TextField()
    published_date = models.IntegerField()
    categories = models.ManyToManyField('Category')
    tasks = models.ManyToManyField('AnaliticTask')
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def only_year(self):
        return self.timestamp.strftime('%Y')

    def StrArticle(self):
        string = "{1},{0}"
        return string.format(self.title, self.author)

    def __str__(self):
        return self.StrArticle()

"""
class Article_Category(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    active = models.BooleanField()


class Article_Task(models.Model):
    task = models.ForeignKey('AnaliticTask', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    activo = models.BooleanField()
"""