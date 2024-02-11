from django.contrib import admin
from .models import Corusel, Biz_haqimizda, Statiska, Tadbir_lavhalari, Toifalash1

@admin.register(Corusel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('Nomi', 'category')


@admin.register(Toifalash1)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nomi',)


@admin.register(Tadbir_lavhalari)
class PostAdmin(admin.ModelAdmin):
    list_display = ('Nomi',)
    
    
@admin.register(Biz_haqimizda)
class PostAdmins(admin.ModelAdmin):
    list_display = ('Nomi',)
    
@admin.register(Statiska)
class StatisPost(admin.ModelAdmin):
    list_display = ('updated',)