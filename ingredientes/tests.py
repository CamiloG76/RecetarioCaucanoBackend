
from django.test import TestCase
from recetas.models import Receta
from .models import Ingrediente


class IngredienteTest(TestCase):

    def setUp(self):
        self.receta = Receta.objects.create(
            nombre='Empanadas de pipian',
            descripcion='Receta tradicional caucana',
            region='Cauca',
            tiempo_preparacion=60,
            dificultad='Media',
            preparacion='Preparar el pipian y rellenar las empanadas'
        )

    def test_crear_ingrediente(self):
        ingrediente = Ingrediente.objects.create(
            receta=self.receta,
            nombre='Papa',
            cantidad='500 gramos'
        )

        self.assertEqual(ingrediente.nombre, 'Papa')
        self.assertEqual(ingrediente.receta, self.receta)
