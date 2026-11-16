
from rest_framework import viewsets
from .models import Ingrediente
from .serializers import IngredienteSerializer


class IngredienteViewSet(viewsets.ModelViewSet):

    queryset = Ingrediente.objects.select_related('receta').all()

    serializer_class = IngredienteSerializer
