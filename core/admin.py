from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('phone_number','address',)  # Note the comma to create a tuple
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('phone_number','address')  # Note the comma to create a tuple
        })
    )


admin.site.register(User, UserAdmin)

# class PharmaCompanyAdmin (admin.ModelAdmin):
#     list_display = ("id","company_name","phone","email")
# admin.site.register(PharmaCompany,PharmaCompanyAdmin)

class MedicineAdmin (admin.ModelAdmin):
    list_display = ("id","name","category","quantity")
admin.site.register(Medicine,MedicineAdmin)

class OrderAdmin (admin.ModelAdmin):
    list_display = ("id","user",'total_price',"order_date","status")
admin.site.register(Order,OrderAdmin)


class PrescriptedOrderAdmin (admin.ModelAdmin):
    list_display = ("orderId",'total_price',"medicine")
admin.site.register(PrescriptedOrder,PrescriptedOrderAdmin)