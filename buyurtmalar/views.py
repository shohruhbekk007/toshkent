from weasyprint import HTML
from django.shortcuts import render
from django_weasyprint.utils import django_url_fetcher
from django.http import HttpResponse
from .models import Sotuv

def pdf_generation(request, queryset):
    try:
        maxsulotlar = Sotuv.objects.all()[queryset-1]
        html_string = render(request, 'home_page.html',  {'maxsulotlar':maxsulotlar }).content.decode('utf-8')

        pdf_file = HTML(string=html_string, url_fetcher=django_url_fetcher).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="home_page.pdf"'
        return response
    except:
        return HttpResponse("Siz mavjud bo'lmagan buyurg kiritdingiz")