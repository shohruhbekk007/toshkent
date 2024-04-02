from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from pasuda_qoshish.models import Toifalash, maxsulot, Taomlar, Stul, Qoshimcha_xizmatlar


class Sale(models.Model):
    sales = models.Manager()
    name = models.CharField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    category_name = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"Name: {self.name} Phone: {self.phone}"

    class Meta:
        verbose_name = 'Sotuv'
        verbose_name_plural = verbose_name + 'lar'
        ordering = ['-id']

class SaleRu(models.Model):
    sale = models.OneToOneField(to=Sale, on_delete=models.CASCADE, related_name='sale_ru', default=None)
    category_name = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"Category name: {self.category_name}"



class Order(models.Model):
    orders = models.Manager()
    product = models.ForeignKey(to=maxsulot, on_delete=models.CASCADE, related_name='orders', blank=True, default=None)
    sale = models.ForeignKey(to=Sale, on_delete=models.CASCADE, related_name='orders')
    count = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product.nomi}"
    
    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = verbose_name + 'lar'
        ordering = ['id']

class OrderRu(models.Model):
    order = models.OneToOneField(to=Order, on_delete=models.CASCADE, related_name='order_ru')



class FoodOrder(models.Model):
    foodorders = models.Manager()
    product = models.ForeignKey(to=Taomlar, on_delete=models.CASCADE, related_name='food_orders')
    sale = models.ForeignKey(to=Sale, on_delete=models.CASCADE, related_name='food_orders')
    count = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product.nomi}"
    
    class Meta:
        verbose_name = 'Ovqat buyurtma'
        verbose_name_plural = verbose_name + 'lar'
        ordering = ['id']

class FoodOrderRu(models.Model):
    order = models.OneToOneField(to=FoodOrder, on_delete=models.CASCADE, related_name='order_ru')



class StulOrder(models.Model):
    stulorders = models.Manager()
    product = models.ForeignKey(to=Stul, on_delete=models.CASCADE, related_name='stul_orders')
    sale = models.ForeignKey(to=Sale, on_delete=models.CASCADE, related_name='stul_orders')
    count = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product.nomi}"
    
    class Meta:
        verbose_name = 'Stul buyurtma'
        verbose_name_plural = verbose_name + 'lar'
        ordering = ['id']

class StulOrderRu(models.Model):
    order = models.OneToOneField(to=StulOrder, on_delete=models.CASCADE, related_name='order_ru')



class ExtraServiceOrder(models.Model):
    serviceorders = models.Manager()
    product = models.ForeignKey(to=Qoshimcha_xizmatlar, on_delete=models.CASCADE, related_name='service_orders')
    sale = models.ForeignKey(to=Sale, on_delete=models.CASCADE, related_name='service_orders')

    def __str__(self) -> str:
        return f"{self.product.nomi}"
    
    class Meta:
        verbose_name = "Qo'shimcha xizmat"
        verbose_name_plural = verbose_name + 'lar'
        ordering = ['id']

class ExtraServiceOrderRu(models.Model):
    order = models.OneToOneField(to=ExtraServiceOrder, on_delete=models.CASCADE, related_name='order_ru')



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Foydalanuvchining elektron pochtasini kiriting')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_admin = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_admin', 'first_name', 'last_name', 'country']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email

