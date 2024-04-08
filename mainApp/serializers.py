from rest_framework import serializers
from .models import *

class ViloyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viloyat
        fields = '__all__'

class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = '__all__'

class FakultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = '__all__'

