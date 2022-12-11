#serializer for toks
from rest_framework import serializers
from .models import Toks


class TokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toks
        fields = '__all__'