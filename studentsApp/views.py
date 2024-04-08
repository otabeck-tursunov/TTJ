from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class StudentsAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='group',
                in_=openapi.IN_QUERY,
                description="Filter by Guruh ID",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='gender',
                in_=openapi.IN_QUERY,
                description="Filter by Jins",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='course',
                in_=openapi.IN_QUERY,
                description="Filter by Kurs",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='region',
                in_=openapi.IN_QUERY,
                description="Filter by Viloyat ID, nom",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='city',
                in_=openapi.IN_QUERY,
                description="Filter by Tuman",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='qarzdor',
                in_=openapi.IN_QUERY,
                description="Filter by Qarzdorlar",
                type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter(
                name='faculty',
                in_=openapi.IN_QUERY,
                description="Filter by Fakultet",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='tutor',
                in_=openapi.IN_QUERY,
                description="Filter by Tutor",
                type=openapi.TYPE_STRING
            ),
        ]
    )
    def get(self, request):
        group = request.query_params.get('group')
        gender = request.query_params.get('jins')
        course = request.query_params.get('course')
        region = request.query_params.get('region')
        city = request.query_params.get('city')
        qarzdor = request.query_params.get('qarzdor')
        faculty = request.query_params.get('faculty')
        tutor = request.query_params.get('tutor')
        students = Student.objects.all()
        if group is not None:
            students = students.filter(guruh__id=group) if group.isdigit() else students.filter(guruh__nom__contains=group)
        if gender is not None:
            students = students.filter(jins=gender)
        if course is not None:
            students = students.filter(guruh__kurs=course)
        if region is not None:
            students = students.filter(tuman__region__id=region) | students.filter(tuman__viloyat__nom=region)
        if city is not None:
            students = students.filter(tuman=city)
        if qarzdor is not None:
            students = students.filter(balans__lt=0) if qarzdor == True else students.filter(balans__gt=0)
        if faculty is not None:
            students = students.filter(guruh__fakultet=faculty)
        if tutor is not None:
            students = students.filter(guruh__tutor__id=tutor)
        data = []
        for student in students:
            student_data = StudentSerializer(student).data
            data.append(student_data)
        return Response(data, status=status.HTTP_200_OK)

