#serializer for toks
from rest_framework import serializers
from .models import Tok


class TokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tok
        fields = '__all__'