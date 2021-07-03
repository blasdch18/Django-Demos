from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(max_length=100 , verbose_name="Nombre Clave", unique=True)
    name =models.CharField(verbose_name="Red Social",max_length=200)
    url =models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name="Fechas de creacion")
    updated = models.DateField(auto_now=True, verbose_name= "Fecha de Edicion")

    class Meta:
        verbose_name="enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']
    
    def __str__(self):
        return self.name
