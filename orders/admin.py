from django.contrib import admin
from .models import User, Sale, Order, SaleRu, OrderRu, FoodOrder, ExtraServiceOrder, StulOrder
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms.models import ModelFormMetaclass
from django.urls import path
from django.http import HttpResponse
from weasyprint import HTML
from django.shortcuts import render
from django.http import Http404
from django_weasyprint.utils import django_url_fetcher


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


class FoodOrderInlineAdmin(admin.TabularInline):
    model = FoodOrder

class ExtraServiceInlineAdmin(admin.TabularInline):
    model = ExtraServiceOrder

class StulInlineAdmin(admin.TabularInline):
    model = StulOrder

class SaleRuInlineAdmin(admin.TabularInline):
    model = SaleRu


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'category_name'
    ]
    inlines = (SaleRuInlineAdmin, ExtraServiceInlineAdmin, FoodOrderInlineAdmin, StulInlineAdmin)
    change_form_template = 'sale_changeform.html'


    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_save'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_delete_link'] = False
        extra_context['show_history_link'] = False

        return super().changeform_view(request, object_id, form_url, extra_context)

    view_on_site = True

    def get_urls(self, **kwargs):
        urls = super().get_urls()
        custom_urls = [
            path(f"printcheck/<int:pk>", self.printcheck, name='printcheck'),
        ]
        return custom_urls + urls

    # actions = ['printcheck']
    
    def printcheck(self, request, *args, **kwargs):
        print(kwargs, args, request)
        try:
            pk = kwargs['pk']
            product = Sale.sales.get(id=pk)
            food_orders = FoodOrder.foodorders.filter(sale_id=pk)
            service_orders = ExtraServiceOrder.serviceorders.filter(sale_id=pk)
            stul_orders = StulOrder.stulorders.filter(sale_id=pk)
            umumiy_baho = 0
            
            for j in food_orders:
                if isinstance(j, FoodOrder):
                    umumiy_baho += j.product.narxi * j.count
            for k in service_orders:
                if isinstance(k, ExtraServiceOrder):
                    umumiy_baho += k.product.narxi
            for l in stul_orders:        
                if isinstance(l, StulOrder):
                    umumiy_baho += l.product.narxi * l.count

            html_string = render(request, 'home_page.html',
                                 {'product':product,
                                  'food_orders': food_orders,
                                  'service_orders': service_orders,
                                  'stul_orders': stul_orders,
                                  'umumiy_baho': umumiy_baho }).content.decode('utf-8')

            pdf_file = HTML(string=html_string, url_fetcher=django_url_fetcher).write_pdf()

            # response = HttpResponse(html_string)
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = 'filename="home_page.pdf"'
            return response
        except Exception as err:
            print('EXception', err)
            raise Http404
