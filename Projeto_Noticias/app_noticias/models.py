from django.db import models

# Create your models here.
class Noticia (models.Model):
    conteudo = models.TextField()