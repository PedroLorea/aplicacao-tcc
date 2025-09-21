from rest_framework import serializers
from api.models import Frete

class FreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frete
        fields = ['id', 'produto']
