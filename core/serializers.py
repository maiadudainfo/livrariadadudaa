from dataclasses import fields

from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Autor, Categoria, Editora, Livro
from media.models import Image
from media.serializers import ImageSerializer


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"


class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)


class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
        capa = ImageSerializer(required=False)