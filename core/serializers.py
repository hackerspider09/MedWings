from rest_framework import serializers
from rest_framework import serializers
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
    