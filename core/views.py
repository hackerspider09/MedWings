from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import *
from .serializers import *
from .utils import *
from .modelUtils import *
import re

from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class AllMedicineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    renderer_classes = [JSONRenderer]
    
    def get_queryset(self):
        category = self.kwargs['category']
        medicineQuerySet = Medicine.objects.filter(category=category)
        return medicineQuerySet

class GetAllOrderViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerSerializer
    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  

    

class SetOrderByModel(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderByModelSerializer
    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]    

    def create(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = user
        serializer.validated_data['status'] = "pending"
        instance = serializer.save()

        instance_id = instance.id
        order_query = Order.objects.get(id=instance_id)

        t = medWing_model(instance.image)
        print(type(t))
        print(t)
        order_list = []
        for key in t:
            item_name = t[key]['item']

            # # Replace spaces with regex wildcard for flexibility
            query = re.sub(r'\s+', '.*', item_name)
            order_dict={}
            try:
                result = Medicine.objects.filter(name__regex=query).first()
                print(result,"++++++++++++++",result.id)
                order_dict['item'] = result.name
                order_dict['price'] = result.price
                print("777777777777777")
                
                if (int(t[key]['quantity']) <= int(result.quantity)):
                    print("66666666666")
                    order_dict['quantity'] = t[key]['quantity']
                    try:
                        print("11111111111")
                        PrescriptedOrder.objects.create(medicine=result,quantity=int(t[key]['quantity']),orderId = order_query)  
                        print("222222222222222")
                        order_dict['isPlaced'] = True  
                    except Exception as e:
                        print("rrrrr",str(e))
                        order_dict['isPlaced'] = False  
                else:
                    order_dict['quantity'] = "Not Available"
            except Exception as e:
                print("rrrrr",str(e))
                pass

            if len(order_dict)>0:
                order_list.append(order_dict)
            

        return  Response({'msg':order_list})
        

        

 