from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from rest_framework import serializers
from .models import Order, Sale, SaleRu, OrderRu, FoodOrder, ExtraServiceOrder, StulOrder
from sahifa.serializer import *


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'product_id',
            'sale_id',
            'count'
        ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = data.copy()

        if hasattr(instance, 'some'):
            pass

        return {
            'uz': data,
            'ru': data_ru
        }


class FoodOrderSerializer(ModelSerializer):
    product = Taom_qoshishSerialzer()
    class Meta:
        model = FoodOrder
        fields = [
            'id',
            'product',
            'sale_id',
            'count'
        ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = data.copy()

        if hasattr(instance, 'some'):
            pass

        return {
            'uz': data,
            'ru': data_ru
        }


class ExtraServiceOrderSerializer(ModelSerializer):
    product = QoshimchaSerializer()
    class Meta:
        model = ExtraServiceOrder
        fields = [
            'id',
            'product',
            'sale_id',
        ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = data.copy()

        if hasattr(instance, 'some'):
            pass

        return {
            'uz': data,
            'ru': data_ru
        }


class StulOrderSerializer(ModelSerializer):
    product = Stul_qoshishSerialzer()
    class Meta:
        model = StulOrder
        fields = [
            'id',
            'product',
            'sale_id',
            'count'
        ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = data.copy()

        if hasattr(instance, 'some'):
            pass

        return {
            'uz': data,
            'ru': data_ru
        }


class SalesListSerializer(ModelSerializer):
    food_orders = SerializerMethodField()
    service_orders = SerializerMethodField()
    stul_orders = SerializerMethodField()

    def get_food_orders(self, obj: Sale):
        try:
            qset = obj.food_orders.all()
            serializer = FoodOrderSerializer(qset, many=True)
            return serializer.data
        except Exception as err:
            print(err)
            return []

    def get_service_orders(self, obj: Sale):
        try:
            qset = obj.service_orders.all()
            serializer = ExtraServiceOrderSerializer(qset, many=True)
            return serializer.data
        except Exception as err:
            print(err)
            return []

    def get_stul_orders(self, obj: Sale):
        try:
            qset = obj.stul_orders.all()
            serializer = StulOrderSerializer(qset, many=True)
            return serializer.data
        except Exception as err:
            print(err)
            return []

    class Meta:
        model = Sale
        fields = [
            'id',
            'name',
            'phone',
            'category_name',
            'food_orders',
            'service_orders',
            'stul_orders',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = super().to_representation(instance)
        if hasattr(instance, 'sale_ru'):
            data_ru['category_name'] = instance.sale_ru.category_name

        return {
            "uz": data,
            "ru": data_ru
        }
