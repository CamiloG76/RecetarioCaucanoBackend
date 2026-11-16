
from django.contrib import admin
from .models import Ingrediente


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nombre',
        'cantidad',
        'receta'
    )

    search_fields = (
        'nombre',
        'receta__nombre'
    )

    list_filter = ('receta',)
