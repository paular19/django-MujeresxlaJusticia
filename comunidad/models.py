from django.db import models

# Create your models here.

class Post (models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='comunidad', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='comunidad'
        verbose_name_plural='comunidades'
    
    def __str__(self):
        return self.titulo
    