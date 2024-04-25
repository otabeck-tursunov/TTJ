from django.urls import path
from .views import *

urlpatterns = [
    path('', XonalarAPIView.as_view()),
]

