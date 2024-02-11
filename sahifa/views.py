from django.http import HttpResponse
from .serializer import Biz_haqimizdaSerilazer, ProductSerializer, CoruselSerilazer, Maxsulot_qoshishSerialzer, Tadbir_lavhaSerilazer, Stul_qoshishSerialzer, StatiskaSerilazer, Taom_qoshishSerialzer, QoshimchaSerializer
from datetime import datetime as d
from buyurtmalar.models import Sotuv
from .models import Biz_haqimizda, Corusel, Statiska, Tadbir_lavhalari
from pasuda_qoshish.models import maxsulot_qoshish, Taomlar, Stul, Qoshimcha_xizmatlar
from rest_framework.generics import ListAPIView, CreateAPIView



vaqt = d.now()

def home(request):
    return HttpResponse(f"<h1>{vaqt}</h1>")


class Carusell(ListAPIView):
    queryset = Corusel.objects.all()
    serializer_class = CoruselSerilazer
 

    
class ProducViews(CreateAPIView):
    queryset = Sotuv.objects.all()
    serializer_class = ProductSerializer
    


class My_photos(ListAPIView):
    queryset = Tadbir_lavhalari.objects.all()
    serializer_class = Tadbir_lavhaSerilazer


class They_aboutList(ListAPIView):
    queryset = Biz_haqimizda.objects.all()
    serializer_class = Biz_haqimizdaSerilazer
    
    
    
class StatiskaViews(ListAPIView):
    queryset = Statiska.objects.all()
    def get_serializer_class(self):
        return StatiskaSerilazer

    
class MaxsulotViews(ListAPIView):
    queryset = maxsulot_qoshish.objects.all()
    serializer_class = Maxsulot_qoshishSerialzer


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