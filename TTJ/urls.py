from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="TTJ uchun API",
        default_version='v1',
        description="Al Xorazmiy nomidagi Toshkent Axborot Texnologiyalari Universiteti Farg'ona Filialini avtomatlashtirish bo'yicha web dastur uchun API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="otabecktursunov@gmail.com"),
        license=openapi.License(name="Mualliflik huquqi asosida"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('users/', include("userApp.urls")),
    path('students/', include("studentsApp.urls")),
]
