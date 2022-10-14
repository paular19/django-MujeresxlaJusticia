from ssl import create_default_context
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Links(models.Model):
    titulo=models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='link'
        verbose_name_plural='links'

    def __str__(self):
        return self.titulo