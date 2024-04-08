from rest_framework import serializers

from studentsApp.models import Student, Guruh


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class GuruhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guruh
        fields = '__all__'
