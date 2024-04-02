from django.contrib import admin
from .models import *


# @admin.register(Corusel)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'category')

# @admin.register(CoruselRu)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'Haqida')


# @admin.register(Toifalash1)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('nomi',)


class EventRuInline(admin.TabularInline):
    model = EventRu

class EventImagesinline(admin.TabularInline):
    model = EventImage

@admin.register(Event)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [EventRuInline, EventImagesinline]



class AboutUsInline(admin.TabularInline):
    model = AboutUsRu

@admin.register(AboutUs)
class PostAdmins(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [AboutUsInline]



@admin.register(Statiska)
class StatisPost(admin.ModelAdmin):
    list_display = ('updated',)
