from rest_framework.viewsets import ModelViewSet
from core.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer, AutorSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer