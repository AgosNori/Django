from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField( max_length=50)
    numero_paginas = serializers.IntegerField()
    fecha_publicacion = serializers.DateField()
    cantidad = serializers.IntegerField()

    def create(self, data):
        return Book.objects.create(**data)

    def update(self, instance, data):
        instance.titulo = data.get('titulo',instance.titulo)
        instance.numero_paginas = data.get('numero_paginas', instance.numero_paginas)
        instance.fecha_publicacion = data.get('fecha_publicacion',instance.fecha_publicacion)
        instance.cantidad = data.get('cantidad', instance.cantidad)
        
        instance.save()
        return instance
