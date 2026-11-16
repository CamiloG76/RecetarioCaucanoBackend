
from rest_framework import serializers
from .models import Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):

    receta_nombre = serializers.CharField(
        source='receta.nombre',
        read_only=True
    )

    class Meta:
        model = Ingrediente
        fields = [
            'id',
            'receta',
            'receta_nombre',
            'nombre',
            'cantidad'
        ]
