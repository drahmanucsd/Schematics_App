from rest_framework import serializers
from .models import Data
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['drawing_number']

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # fields = '__all__'
        fields = [
            'drawing_number',
            'descr'
        ]