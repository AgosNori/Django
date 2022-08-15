from django.db import models

# Create your models here.
class Book(models.Model):
    titulo = models.CharField( max_length=50)
    numero_paginas = models.IntegerField()
    fecha_publicacion = models.DateField()
    cantidad = models.IntegerField()

    def __str__(self) :
        return self.titulo
