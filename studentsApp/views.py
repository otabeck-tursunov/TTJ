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
                name='jins',
                in_=openapi.IN_QUERY,
                description="Filter by Jins. True - Male; False - Female",
                type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter(
                name='kurs',
                in_=openapi.IN_QUERY,
                description="Filter by Kurs",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='viloyat_id',
                in_=openapi.IN_QUERY,
                description="Filter by Viloyat ID",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='tuman_id',
                in_=openapi.IN_QUERY,
                description="Filter by Tuman ID",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='qarzdor',
                in_=openapi.IN_QUERY,
                description="Filter by Qarzdorlar",
                type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter(
                name='faculty_id',
                in_=openapi.IN_QUERY,
                description="Filter by Fakultet ID",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='tutor_id',
                in_=openapi.IN_QUERY,
                description="Filter by Tutor ID",
                type=openapi.TYPE_STRING
            ),
        ]
    )
    def get(self, request):
        group = request.query_params.get('group')
        jins = request.query_params.get('jins')
        kurs = request.query_params.get('kurs')
        tuman_id = request.query_params.get('tuman_id')
        viloyat_id = request.query_params.get('viloyat_id')
        qarzdor = request.query_params.get('qarzdor')
        faculty_id = request.query_params.get('faculty_id')
        tutor_id = request.query_params.get('tutor_id')

        students = Student.objects.all()

        if group is not None:
            students = students.filter(guruh__id=group) if group.isdigit() else students.filter(
                guruh__nom__contains=group)
        if jins is not None:
            if jins == "true":
                students = students.filter(jins="erkak")
            elif jins == "false":
                students = students.filter(jins="ayol")
        if kurs is not None:
            students = students.filter(guruh__kurs=kurs)
        if tuman_id is not None:
            students = students.filter(tuman__id=tuman_id)
        if viloyat_id is not None:
            students = students.filter(tuman__viloyat__id=viloyat_id)
        if qarzdor is not None:
            students = students.filter(balans__lt=0) if qarzdor == True else students.filter(balans__gte=0)
        if faculty_id is not None:
            students = students.filter(guruh__fakultet__id=faculty_id)
        if tutor_id is not None:
            students = students.filter(guruh__tutor__id=tutor_id)

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
