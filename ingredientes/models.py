
from django.db import models
from recetas.models import Receta


class Ingrediente(models.Model):

    receta = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE,
        related_name='ingredientes'
    )

    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre del ingrediente"
    )

    cantidad = models.CharField(
        max_length=100,
        verbose_name="Cantidad del ingrediente"
    )

    def __str__(self):
        return f"{self.nombre} - {self.receta.nombre}"

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"
        ordering = ['nombre']
