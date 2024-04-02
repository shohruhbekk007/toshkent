from weasyprint import HTML
from django.shortcuts import render
from django_weasyprint.utils import django_url_fetcher
from django.http import HttpResponse, request
from .models import Sale, Order, Toifalash, ExtraServiceOrder, FoodOrder, StulOrder
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from .serializers import OrderSerializer, SalesListSerializer, FoodOrderSerializer, ExtraServiceOrderSerializer, StulOrderSerializer
from django.http import Http404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status



class SalesViewSet(ModelViewSet):
    queryset = Sale.sales.all().order_by('-id')
    serializer_class = SalesListSerializer


class SaleView(DestroyAPIView):
    serializer_class = SalesListSerializer

    def get_object(self):
        sale_id = self.kwargs.get('pk')
        try:
            sale = Sale.sales.get(id=sale_id)
            return sale
        except Exception:
            raise Http404

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# class OrdersViewSet(ModelViewSet):
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         sale_id = self.kwargs.get('pk')
#         try:
#             qset = Order.orders.filter(sale_id=sale_id)
#             return qset
#         except Order.DoesNotExist:
#             raise Http404


class FoodOrdersViewSet(ModelViewSet):
    serializer_class = FoodOrderSerializer

    def get_queryset(self):
        sale_id = self.kwargs.get('pk')
        try:
            qset = FoodOrder.foodorders.filter(sale_id=sale_id)
            return qset
        except Order.DoesNotExist:
            raise Http404


class ExtraServiceOrdersViewSet(ModelViewSet):
    serializer_class = ExtraServiceOrderSerializer

    def get_queryset(self):
        sale_id = self.kwargs.get('pk')
        try:
            qset = ExtraServiceOrder.serviceorders.filter(sale_id=sale_id)
            return qset
        except Order.DoesNotExist:
            raise Http404


class StulOrdersViewSet(ModelViewSet):
    serializer_class = StulOrderSerializer

    def get_queryset(self):
        sale_id = self.kwargs.get('pk')
        try:
            qset = StulOrder.stulorders.filter(sale_id=sale_id)
            return qset
        except Order.DoesNotExist:
            raise Http404


class SaleCreateApiView(CreateAPIView):
    serializer_class = SalesListSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class OrderView(DestroyAPIView, CreateAPIView):
#     serializer_class = OrderSerializer

#     def get_object(self):
#         order_id = self.kwargs.get('order_id')
#         try:
#             b = Order.orders.get(id=order_id)
#             return b
#         except Order.DoesNotExist:
#             raise Http404

#     def get(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         sale_id = request.data.get('sale_id')
#         category_id = request.data.get('category_id')

#         if sale_id is None or category_id is None:
#             return Response({"error": "sale_id va category_id kiritilishi shart"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             sale = Sale.sales.get(id=sale_id)
#             category = Toifalash.objects.get(id=category_id)
#         except Sale.DoesNotExist or Toifalash.DoesNotExist:
#             return Response({"error": "Bunday Sale yoki category topilmadi"}, status=status.HTTP_400_BAD_REQUEST)

#         request.data['sale'] = Sale.id
#         request.data['category'] = category.id
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)
