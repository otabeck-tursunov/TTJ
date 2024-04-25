from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class XonalarAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='ordering',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=['id', 'raqam', 'qavat', 'joylar_soni'],
                default='id'
            ),
            openapi.Parameter(
                'search', in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Raqami bo\'yicha qidirish',
            ),
            openapi.Parameter(
                'qavat', in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='Raqami bo\'yicha filterlash',
            )
        ]
    )
    def get(self, request):
        ordering = request.query_params.get('ordering', 'id')
        search = request.query_params.get('search', None)
        qavat = request.query_params.get('qavat', None)

        xonalar = Xona.objects.all().order_by(ordering)

        if search is not None:
            xonalar = xonalar.filter(raqam__icontains=search)

        if qavat is not None:
            xonalar = xonalar.filter(qavat=qavat)
        serializer = XonaSerializer(xonalar, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=XonaSerializer,
    )
    def post(self, request):
        serializer = XonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)