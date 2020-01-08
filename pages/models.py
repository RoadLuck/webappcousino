from django.db import models
from ckeditor.fields import RichTextField
from . import managers

class Page(models.Model):
    EVENT_TYPE = (
    ("event", "EVENTO"),
    ("theater", "OBRA"),
)

    event_type = models.CharField(verbose_name="Tipo de Evento", max_length=100,choices=EVENT_TYPE,default="EVENTO",null=True)
    title = models.CharField(verbose_name="Título", max_length=200)
    description = models.CharField(verbose_name="Descripcion", max_length=200,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)
    content = RichTextField(verbose_name="Contenido")
    date_init = models.DateField(verbose_name="Inicio Evento",null=True)
    date_finish = models.DateField(verbose_name="Termino Evento",null=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    active = models.BooleanField(null=True, default=True)


    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
