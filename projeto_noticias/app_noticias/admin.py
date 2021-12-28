from django.contrib import admin
from app_noticias.models import Categoria, Status, Artigo
from django.contrib.auth.models import User, Permission
from django.http import HttpResponse
from app_noticias.forms import ArtigoAdminForm
from django.utils.html import format_html



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_filter = 'categoria', 'status'
    list_per_page = 10
    form = ArtigoAdminForm
