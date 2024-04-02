from django.urls import path
from .views import *


urlpatterns = [
    # path('', home, name="home" ),
    path('corusel', Carusell.as_view(), name="corusell"),
    path('events', EventsList.as_view(), name='my_photos'),
    path('about_us', AboutUsList.as_view(), name='they_about'),
    path('maxsulot', MaxsulotViews.as_view(), name='maxsulot'),
    path('statiska', StatiskaViews.as_view(), name='statiska'), 
    path('jihozlar', QoshimchaViews.as_view(), name="jihozlar"),
    path('taomlar', TaomlarViews.as_view(), name='taomlar'),
    path('stulstol', StulViews.as_view(), name="stul"),    
]
