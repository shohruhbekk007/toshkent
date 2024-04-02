from django.db import models


class Toifalash(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nomi
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Toifa'
        verbose_name_plural = verbose_name + 'lar'

class ToifalashRu(models.Model):
    toifalash = models.OneToOneField(to=Toifalash, on_delete=models.CASCADE, related_name='toifalash_ru')
    nomi = models.CharField(max_length=255)



class maxsulot(models.Model):
    nomi = models.CharField(max_length=255)
    olchami = models.CharField(max_length=20, null =True, blank=True)
    Rasm = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    narxi = models.IntegerField()
    toifasi = models.ForeignKey(Toifalash, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nomi
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Maxsulot'
        verbose_name_plural = verbose_name + 'lar'

class maxsulotRu(models.Model):
    maxsulot = models.OneToOneField(to=maxsulot, on_delete=models.CASCADE, related_name='maxsulot_ru')
    nomi = models.CharField(max_length=255)



class Taomlar(models.Model):
    nomi = models.CharField(max_length=100)
    Rasm = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    narxi = models.IntegerField()
    toifasi = models.ForeignKey(Toifalash, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nomi
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Taom'
        verbose_name_plural = verbose_name + 'lar'

class TaomlarRu(models.Model):
    meal = models.OneToOneField(to=Taomlar, on_delete=models.CASCADE, related_name='meal_ru')
    nomi = models.CharField(max_length=255)



class Stul(models.Model):
    nomi = models.CharField(max_length=100)
    olchami = models.CharField(max_length=20, null =True, blank=True)
    Rasm = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    narxi = models.IntegerField()
    toifasi = models.ForeignKey(Toifalash, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nomi + ' ' + self.olchami
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Stul'
        verbose_name_plural = verbose_name + 'lar'

class StulRu(models.Model):
    chair = models.OneToOneField(to=Stul, on_delete=models.CASCADE, related_name='chair_ru')
    nomi = models.CharField(max_length=255)



class Qoshimcha_xizmatlar(models.Model):
    nomi = models.CharField(max_length=120)
    narxi = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.nomi
    
    class Meta:
        ordering = ['id']
        verbose_name = "Qo'shimcha xizmat"
        verbose_name_plural = verbose_name + 'lar'

class QoshimchaXizmatlarRu(models.Model):
    service = models.OneToOneField(to=Qoshimcha_xizmatlar, on_delete=models.CASCADE, related_name='service_ru')
    nomi = models.CharField(max_length=255)
