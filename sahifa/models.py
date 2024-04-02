from django.db import models


class Toifalash1(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nomi



class Corusel(models.Model):
    Nomi = models.CharField(max_length=68)
    Haqida = models.CharField(max_length=255)
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    category = models.ForeignKey(Toifalash1, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Nomi

    class Meta:
        ordering = ['id']
    
class CoruselRu(models.Model):
    carousel = models.OneToOneField(to=Corusel, on_delete=models.CASCADE, related_name='corusel_ru')
    Nomi = models.CharField(max_length=68)
    Haqida = models.CharField(max_length=255)



class Event(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Tadbir'
        verbose_name_plural = verbose_name + 'lar'

class EventRu(models.Model):
    event = models.OneToOneField(to=Event, on_delete=models.CASCADE, related_name='event_ru')
    title = models.CharField(max_length=255)

class EventImage(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, related_name='images')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)



class AboutUs(models.Model):
    title = models.CharField(max_length=65)
    comment = models.CharField(max_length=255)
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Biz haqimizda'
        verbose_name_plural = verbose_name

class AboutUsRu(models.Model):
    about_us = models.OneToOneField(to=AboutUs, on_delete=models.CASCADE, related_name='about_us_ru')
    title = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)



class Statiska(models.Model):
    soni = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"oxirgi yangilanishi {self.updated}"
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Statistika'
        verbose_name_plural = verbose_name
