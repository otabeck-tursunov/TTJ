from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import ViloyatSerializer, TumanSerializer, FakultetSerializer


class ViloyatlarAPIView(APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'ordering', openapi.IN_QUERY,
            description="Tartiblash ustuni",
            type=openapi.TYPE_STRING,
            enum=["nom", "id"],
            default="id"
        ),
        openapi.Parameter(
            'search', openapi.IN_QUERY,
            description="Nomi bo'yicha qidirish",
            type=openapi.TYPE_STRING,
        )
    ])
    def get(self, request):
        ordering = request.query_params.get('ordering', 'id')
        search = request.query_params.get('search', None)

        viloyatlar = Viloyat.objects.all().order_by(ordering)

        if search:
            viloyatlar = viloyatlar.filter(Q(nom__icontains=search))

        serializer = ViloyatSerializer(viloyatlar, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ViloyatSerializer,
    )
    def post(self, request):
        serializer = ViloyatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TumanlarAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'ordering', openapi.IN_QUERY,
                description="Tartiblash ustuni",
                type=openapi.TYPE_STRING,
                enum=["id", "nom", "viloyat_id"],
                default="id"
            ),
            openapi.Parameter(
                'search', openapi.IN_QUERY,
                description="Nomi bo'yicha qidirish",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'viloyat_id', openapi.IN_QUERY,
                description="Viloyat ID bo'yicha filter",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                'turi', openapi.IN_QUERY,
                description="Turi bo'yicha filter",
                type=openapi.TYPE_STRING,
                enum=["tuman", "shahar"],
                default="tuman"
            )
        ]
    )
    def get(self, request):
        ordering = request.query_params.get('ordering', 'id')
        search = request.query_params.get('search', None)
        viloyat_id = request.query_params.get('viloyat_id', None)
        turi = request.query_params.get('turi', None)

        if ordering == 'viloyat_id':
            tumanlar = Tuman.objects.all().order_by("viloyat__id")
        else:
            tumanlar = Tuman.objects.all().order_by(ordering)

        if search is not None:
            tumanlar = tumanlar.filter(Q(nom__icontains=search))

        if viloyat_id is not None:
            tumanlar = tumanlar.filter(viloyat__id=viloyat_id)

        if turi is not None:
            tumanlar = tumanlar.filter(turi=turi)

        serializer = TumanSerializer(tumanlar, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=TumanSerializer,
    )
    def post(self, request):
        serializer = TumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FakultetlarAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'ordering', openapi.IN_QUERY,
                description="Tartiblash ustuni",
                type=openapi.TYPE_STRING,
                enum=["nom", "id"],
                default="id"
            ),
            openapi.Parameter(
                'search', openapi.IN_QUERY,
                description="Nomi bo'yicha qidirish",
                type=openapi.TYPE_STRING,
            )
        ]
    )
    def get(self, request):
        ordering = request.query_params.get('ordering', 'id')
        search = request.query_params.get('search', None)

        fakultetlar = Fakultet.objects.all().order_by(ordering)

        if search:
            fakultetlar = fakultetlar.filter(Q(nom__icontains=search))

        serializer = FakultetSerializer(fakultetlar, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=FakultetSerializer,
    )
    def post(self, request):
        serializer = FakultetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
