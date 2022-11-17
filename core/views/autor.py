from rest_framework.viewsets import ModelViewSet
from core.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer, AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer