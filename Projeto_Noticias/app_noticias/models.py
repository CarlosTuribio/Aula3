from django.db import models

# Create your models here.
class Noticia(models.Model):
    conteudo =  models.TextField()
    autor = models.CharField('autor', max_length=128 , blank=True, null=True)
    titulo = models.CharField('título', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.conteudo

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    
    

