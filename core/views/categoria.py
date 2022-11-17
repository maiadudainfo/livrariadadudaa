from rest_framework.viewsets import ModelViewSet
from core.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer, AutorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer