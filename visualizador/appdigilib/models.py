from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    categoria= models.CharField(max_length=200)

class AnaliticTask(models.Model):
    task = models.CharField(max_length=250)

class Articulo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    task = models.ForeignKey(AnaliticTask, on_delete=models.CASCADE)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    doi = models.CharField(max_length=250)
    text = models.TextField()
    #created_date = models.DateTimeField(
    #        default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True, unique_for_year=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title