from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.register(Viloyat)
admin.site.register(Tuman)
admin.site.register(Fakultet)
admin.site.unregister(Group)