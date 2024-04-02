from django.http import HttpResponse
from .serializer import *
from datetime import datetime as d
from orders.models import Sale
from .models import *
from pasuda_qoshish.models import maxsulot, Taomlar, Stul, Qoshimcha_xizmatlar
from rest_framework.generics import ListAPIView, CreateAPIView



vaqt = d.now()

def home(request):
    return HttpResponse(f"<h1>{vaqt}</h1>")


class Carusell(ListAPIView):
    queryset = Corusel.objects.all()
    serializer_class = CoruselSerilazer


class EventsList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerilazer


class AboutUsList(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerilazer

    
class StatiskaViews(ListAPIView):
    queryset = Statiska.objects.all()
    def get_serializer_class(self):
        return StatiskaSerilazer

    
class MaxsulotViews(ListAPIView):
    queryset = maxsulot.objects.all()
    serializer_class = maxsulotSerialzer


class StulViews(ListAPIView):
    queryset = Stul.objects.all()
    def get_serializer_class(self):
        return Stul_qoshishSerialzer

class TaomlarViews(ListAPIView):
    queryset = Taomlar.objects.all()
    def get_serializer_class(self):
        return Taom_qoshishSerialzer
    
    
class QoshimchaViews(ListAPIView):
    queryset = Qoshimcha_xizmatlar.objects.all()
    def get_serializer_class(self):
        return QoshimchaSerializer