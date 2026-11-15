from django.contrib import admin
from .models import Receta


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tiempo_preparacion', 'dificultad')
    search_fields = ('nombre',)
    list_filter = ('dificultad',)
