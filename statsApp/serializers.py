from rest_framework import serializers
from .models import *


class BandQilishSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandQilish
        fields = '__all__'


class TolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tolov
        fields = '__all__'
