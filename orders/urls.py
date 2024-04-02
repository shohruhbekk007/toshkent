from django.urls import path
from .views import *
from .admin import SaleAdmin


urlpatterns = [
    path('sales/', SalesViewSet.as_view({'get':'list'}), name='sales'),
    path('sales/sale/', SaleCreateApiView.as_view(), name='salecreate'),
    path('sales/sale/<int:pk>/', SaleView.as_view(), name='sale'),
    # path('sales/sale/<int:pk>/orders/', OrdersViewSet.as_view({'get': 'list'}), name='orders'),
    path('sales/sale/<int:pk>/foodorders/', FoodOrdersViewSet.as_view({'get': 'list'}), name='foodorders'),
    path('sales/sale/<int:pk>/serviceorders/', ExtraServiceOrdersViewSet.as_view({'get': 'list'}), name='serviceorders'),
    path('sales/sale/<int:pk>/stulorders/', StulOrdersViewSet.as_view({'get': 'list'}), name='stulorders'),
    # path('sales/sale/<int:pk>/orders/order/<int:order_id>/', OrderView.as_view(), name='order'),
]

