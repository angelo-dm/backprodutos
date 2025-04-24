from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    imagem = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'imagem']

    def get_imagem(self, obj):
        request = self.context.get('request')
        if obj.imagem and hasattr(obj.imagem, 'url'):
            return request.build_absolute_uri(obj.imagem.url)
        else:
            return None