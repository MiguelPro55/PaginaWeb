from django.contrib import admin
from .models import Marca, Celular,Carrito
# Register your models here.

class CelularAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','precio','memoria','camarafrontal','camaratrasera','cpu','os','srcimg')

admin.site.register(Marca)
admin.site.register(Celular, CelularAdmin)
admin.site.register(Carrito)