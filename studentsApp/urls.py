from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentsAPIView.as_view())
]