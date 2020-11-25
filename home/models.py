from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class Categoria(models.Model):
    nome_cat = models.CharField(max_length=255)
    link = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.nome_cat

class User(models.Model):
    nome = models.CharField(max_length=255)
    resumo = models.CharField(default=" ", blank=True, null=True, max_length=100)
    imagem = models.ImageField(upload_to='blog', blank=True, default='/blog/white_image.jpg', null=True)
    data_nasc = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = RichTextField()
    resumo = models.CharField(default=" ", blank=True, null=True, max_length=100)
    link = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='media', blank=True, default='white_image.jpg')
    data = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo



