from django.contrib import admin
from .models import User, Sotuv
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect


# admin.site.register(User)


class CustomUserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'user_admin', 'first_name', 'last_name', 'country', 'photo', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'password1', 'password2'),
            },
        ),
    )
    form = CustomUserCreationForm
    list_display = ('id', 'email', 'user_admin', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    ordering = ('id',)



class MyModelAdmin(admin.ModelAdmin):
    actions = ['chek']

    def chek(self, request, queryset):
        selected_ids = list(queryset.values_list('id', flat=True))
        url = reverse('pdf_generation', kwargs={'queryset': ','.join(map(str, selected_ids))})
        return HttpResponseRedirect(url)

    chek.short_description = "Chek olish"

admin.site.register(Sotuv, MyModelAdmin)


