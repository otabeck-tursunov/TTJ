from django.urls import path
from .views import *

urlpatterns = [
    path('viloyatlar/', ViloyatlarAPIView.as_view()),
    path('tumanlar/', TumanlarAPIView.as_view()),
    path('fakultetlar/', FakultetlarAPIView.as_view()),
]

