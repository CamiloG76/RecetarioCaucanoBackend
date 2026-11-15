from django.db import models


class Receta(models.Model):

    DIFICULTADES = [
        ('Facil', 'Fácil'),
        ('Media', 'Media'),
        ('Dificil', 'Difícil'),
    ]

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    tiempo_preparacion = models.PositiveIntegerField()
    dificultad = models.CharField(
        max_length=20,
        choices=DIFICULTADES,
        default='Facil'
    )

    def __str__(self):
        return self.nombre
