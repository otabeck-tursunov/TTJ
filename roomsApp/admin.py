from django.contrib import admin
from .models import *


class JoyTabularInline(admin.TabularInline):
    model = Joy


class RoomAdmin(admin.ModelAdmin):
    inlines = [JoyTabularInline]


admin.site.register(Xona, RoomAdmin)
admin.site.register(Joy)
