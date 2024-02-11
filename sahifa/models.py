from django.db import models


class Toifalash1(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nomi


class Corusel(models.Model):
    Nomi = models.CharField(max_length=68)
    Haqida = models.CharField(max_length=255)
    Rasm = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    category = models.ForeignKey(Toifalash1, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Nomi
    



class Tadbir_lavhalari(models.Model):
    Nomi = models.CharField(max_length=60)
    Rasmlar = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.Nomi


class Biz_haqimizda(models.Model):
    Nomi = models.CharField(max_length=65)
    komment = models.CharField(max_length=255)
    Rasm = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    



class Statiska(models.Model):
    soni = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"oxirgi yangilanishi {self.updated}"
