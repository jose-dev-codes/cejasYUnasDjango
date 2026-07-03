from django.contrib import admin
from .models import Usuarios, Servicios, Citas

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Servicios)
admin.site.register(Citas)
