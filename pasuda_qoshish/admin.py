from django.contrib import admin
from .models import Toifalash, maxsulot_qoshish, Qoshimcha_xizmatlar, Stul, Taomlar
# from .models import AlohidaPasuda, CofeBreak, Golf, Inventarlar, KumushEskiPasuda, LacostaPasuda, MaterialMahsulotlar, OqTillaPasuda, Set_Pasuda, YashilPasuda, Stol_stul, Materialli_mahsulotlar


admin.site.register(Toifalash)

@admin.register(maxsulot_qoshish)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'olchami', 'toifasi')

@admin.register(Qoshimcha_xizmatlar)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'olchami')

@admin.register(Stul)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'olchami', 'toifasi')

@admin.register(Taomlar)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'olchami', 'toifasi')



# @admin.register(Set_Pasuda)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')


# @admin.register(AlohidaPasuda)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')


# @admin.register(CofeBreak)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')

# @admin.register(Golf)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')

# @admin.register(Inventarlar)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')

# @admin.register(KumushEskiPasuda)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')

# @admin.register(LacostaPasuda)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')


# @admin.register(MaterialMahsulotlar)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')

# @admin.register(OqTillaPasuda)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')

# @admin.register(YashilPasuda)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')

# @admin.register(Materialli_mahsulotlar)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('Nomi', 'tarela_olchami', 'narxi')

# @admin.register(Stol_stul)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('nomi', 'stol_olchami', 'narxi')


# Register your models here.
