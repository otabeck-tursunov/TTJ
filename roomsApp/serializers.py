from rest_framework import serializers
from .models import *

class XonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xona
        fields = '__all__'

class JoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Joy
        fields = '__all__'

class JihozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jihoz
        fields = '__all__'

