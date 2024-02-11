from django.urls import path
from .views import home, Carusell,  My_photos, They_aboutList, ProducViews, MaxsulotViews, StatiskaViews, TaomlarViews, StulViews, QoshimchaViews
from buyurtmalar.views import pdf_generation

urlpatterns = [
    path('', home, name="home" ),
    path('corusel', Carusell.as_view(), name="corusellls"),
    path('Otkazilgan_tadbirlar', My_photos.as_view(), name='my_photos'),
    path('Biz_haqimizda', They_aboutList.as_view(), name='they_about'),
    path('products', ProducViews.as_view(), name='product'),
    path('maxsulot_qoshish', MaxsulotViews.as_view(), name='maxsulot'),
    path('statiska', StatiskaViews.as_view(), name='statiska'), 
    path('pdf_generation/<int:queryset>/', pdf_generation, name='pdf_generation'),  
    path('jihozlar', QoshimchaViews.as_view(), name="jihozlar"),
    path('taomlar', TaomlarViews.as_view(), name='taomlar'),
    path('stulstol', StulViews.as_view(), name="stul"),    
]
