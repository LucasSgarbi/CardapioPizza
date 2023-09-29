from django.contrib import admin
from .models import Categoria, Combo, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'ativo')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'categoria')


@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ('nome', 'total')

