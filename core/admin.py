from django.contrib import admin
from .models import Bebida


@admin.register(Bebida)
class AdminBebidas(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'tipo')

# Register your models here.
