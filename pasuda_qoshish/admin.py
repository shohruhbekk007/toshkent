from django.contrib import admin
from .models import *


class CategoryInline(admin.TabularInline):
    model = ToifalashRu

@admin.register(Toifalash)
class ToifaAdmin(admin.ModelAdmin):
    list_display = ['nomi']
    inlines = [CategoryInline]



class MaxsulotInline(admin.TabularInline):
    model = maxsulotRu

@admin.register(maxsulot)
class AddPostAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'olchami', 'Rasm', 'narxi', 'toifasi')
    inlines = [MaxsulotInline]


class ExtraServiceinline(admin.TabularInline):
    model = QoshimchaXizmatlarRu

@admin.register(Qoshimcha_xizmatlar)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi', 'created')
    inlines = [ExtraServiceinline]


class TableInline(admin.TabularInline):
    model = StulRu

@admin.register(Stul)
class TableAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'Rasm', 'narxi', 'olchami', 'toifasi')
    inlines = [TableInline]



class FoodsInline(admin.TabularInline):
    model = TaomlarRu

@admin.register(Taomlar)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'Rasm', 'narxi', 'toifasi')
    inlines = [FoodsInline]


