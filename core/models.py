from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

def Upload_to_MedWings(instance,filename):
    return str(f"MedWings/{instance.category}/{filename}")


def Upload_to_PharmaCompany(instance,filename):
    return str(f"PharmaCompany/{filename}")


def Upload_to_UserMedicine(instance,filename):
    return str(f"Order/{instance.user}/{filename}")

def generate_id():
    id = str(uuid.uuid4())[:6].upper() 
    return id



class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    address = models.TextField()


# class PharmaCompany(models.Model):
#     company_name = models.CharField(max_length=50)
#     website = models.URLField(max_length=200)
#     email = models.EmailField()
#     phone = models.CharField(max_length=13)
#     phone_optional = models.CharField(max_length=13,null=True,blank=True)
#     logo = models.ImageField(upload_to=Upload_to_PharmaCompany, height_field=None, width_field=None, max_length=None,null=True,blank=True)

#     def __str__(self) -> str:
#         return self.company_name



# face and hair  
# eqiu
# Medicine
# hygine

class Medicine(models.Model):
    id = models.CharField(max_length=6,default=generate_id,primary_key=True,editable=False)
    # company = models.ForeignKey(PharmaCompany, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price  = models.PositiveIntegerField(default=500)
    image = models.ImageField( upload_to=Upload_to_MedWings, height_field=None, width_field=None, max_length=None,null=True,blank=True)
    category_choice = (
        ('equipment','equipment'),
        ('medicine','medicine'),
        ('hygiene','hygiene'),
        ('face_and_hair', 'face and hair'),
    )

    category  = models.CharField( max_length=15,choices=category_choice)

    def __str__(self) -> str:
        return self.name




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Upload_to_UserMedicine, height_field=None, width_field=None, max_length=None,blank=True,null=True)
    order_date = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status_choice = (
        ('pending','pending'),
        ('placed','placed'),
        ('processed','processed'),
        ('delivered','delivered'),
        ('canceld','canceld')
    )

    status  = models.CharField( max_length=10,choices=status_choice)


    def save(self, *args, **kwargs):
        '''implement after 2 day if order is not placed then delet it '''
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username
    

class PrescriptedOrder(models.Model):
    orderId = models.ForeignKey(Order,  on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0) 

    
            