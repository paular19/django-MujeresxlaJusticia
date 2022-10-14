from django.db import models

# Create your models here.
class Jurisp(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion= models.TextField(max_length=400)
    field = models.FileField(upload_to = None, max_length = 254, null=True, blank=True)

    class Meta:
        verbose_name='jurisp'
        verbose_name_plural='jurisps'

    def __str__(self):
        return self.titulo

