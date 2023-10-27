from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"

class OrderSerializerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderByModelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Order
        fields = ["image"]
    

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate_username(self, value):
        # Check if the username is already taken
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username is already exists.')
        return value



class OrderItemSerializer(serializers.Serializer):
    item = serializers.CharField()
    quantity = serializers.IntegerField()

class OrderRequestSerializer(serializers.Serializer):
    order = OrderItemSerializer(many=True)

class PrescriptedOrderSerializer(serializers.ModelSerializer):
    medicine_name = serializers.SerializerMethodField()

    class Meta:
        model = PrescriptedOrder
        fields = ('id', 'quantity', 'total_price', 'orderId', 'medicine', 'medicine_name')

    def get_medicine_name(self, obj):
        return obj.medicine.name

