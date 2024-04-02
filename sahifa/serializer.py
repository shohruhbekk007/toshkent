from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField
from orders.models import Sale
from pasuda_qoshish.models import Toifalash, maxsulot, Stul, Taomlar, Qoshimcha_xizmatlar
from .models import *


class Toifalash1Serializer(ModelSerializer):
    class Meta:
        model = Toifalash1
        fields = '__all__'

class CoruselSerilazer(ModelSerializer):
    category = SerializerMethodField()

    def get_category(self, obj):
        return obj.category.nomi

    class Meta:
        model = Corusel
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = super().to_representation(instance)

        if hasattr(instance, 'corusel_ru'):
            data_ru['title'] = instance.corusel_ru.Nomi
            data_ru['desc'] = instance.corusel_ru.Haqida

        return {
            'uz': data,
            'ru': data_ru
        }


class AboutUsSerilazer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = data.copy()

        if hasattr(instance, 'about_us_ru'):
            data_ru['title'] = instance.about_us_ru.title
            data_ru['comment'] = instance.about_us_ru.comment
        
        return {
            'uz': data,
            'ru': data_ru
        }


class StatiskaSerilazer(ModelSerializer):
    class Meta:
        model = Statiska
        fields = '__all__'



class EventPhotosSerializer(ModelSerializer):
    class Meta:
        model = EventImage
        fields = [
            'id',
            'photo'
        ]


class EventSerilazer(ModelSerializer):
    photos = SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'created',
            'photos',
        ]
    
    def get_photos(self, obj):
        qset = obj.images.all()
        serializer = EventPhotosSerializer(qset, many=True)
        return serializer.data
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = super().to_representation(instance)
        
        if hasattr(instance, 'event_ru'):
            data_ru['title'] = instance.event_ru.title
        
        return {
            'uz': data,
            'ru': data_ru
        }


        
        
class ToifalshSerializer(ModelSerializer):
    class Meta:
        model = Toifalash
        fields = [
            'id',
            'nomi'
        ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = super().to_representation(instance)
        if hasattr(instance, 'toifalash_ru'):
            data_ru['nomi'] = instance.toifalash_ru.nomi

        return {
            'uz': data,
            'ru': data_ru
        }



class QoshimchaSerializer(ModelSerializer):
    class Meta:
        model = Qoshimcha_xizmatlar
        fields = ['id', 'nomi']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = data.copy()
        if hasattr(instance, 'service_ru'):
            data_ru['nomi'] = instance.service_ru.nomi
        
        return {
            'uz': data,
            'ru': data_ru
        }


class Stul_qoshishSerialzer(ModelSerializer):
    toifasi = ToifalshSerializer()
    class Meta:
        model = maxsulot
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = data.copy()

        if hasattr(instance, 'chair_ru'):
            data_ru['nomi'] = instance.chair_ru.nomi
        
        return {
            'uz': data,
            'ru': data_ru
        }



class maxsulotSerialzer(ModelSerializer):
    toifasi = ToifalshSerializer()
    class Meta:
        model = Stul
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = data.copy()

        if hasattr(instance, 'maxsulot_ru'):
            data_ru['nomi'] = instance.maxsulot_ru.nomi
        
        return {
            'uz': data,
            'ru': data_ru
        }


class Taom_qoshishSerialzer(ModelSerializer):
    toifasi = ToifalshSerializer()
    class Meta:
        model = Taomlar
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data_ru = data.copy()
        if hasattr(instance, 'meal_ru'):
            data_ru['nomi'] = instance.meal_ru.nomi
        
        return {
            'uz': data,
            'ru': data_ru
        }
