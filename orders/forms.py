from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'user_admin', 'first_name', 'last_name', 'country', 'photo', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
