from django.contrib import admin
from . models import Customer, Thing, Order
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_filter = ['created_at']
    search_fields = ['name', 'tel']

    readonly_fields = ['created_at']

    fieldsets = [
        (
            'Customer',
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Контактная информация',
                'fields': ['email', 'tel', 'address'],
            },
        ),
        (
            'Other info',
            {
                'description': 'Прочее',
                'fields': ['created_at'],
            }
        ),
    ]


class ThingAdmin(admin.ModelAdmin):
    @admin.action(description='сбросить количество')
    def reset_quantity(modeladmin,request,quesryset):
        # quesryset.update(contetent='')
        quesryset.update(quantity= 123456)



    list_display = ['thing_name', 'description']
    ordering = ['thing_name', 'price', 'quantity']
    list_filter = ['thing_added_date', 'thing_name']
    search_fields = ['thing_name', 'price', 'quantity']
    actions = ['reset_quantity']


    readonly_fields = ['thing_added_date']

    fieldsets = [
        (
            'Thing',
            {
                'classes': ['wide'],
                'fields': ['thing_name'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Бизнес инфо',
                'fields': ['price', 'quantity'],
            },
        ),
        (
            'Other info',
            {
                'description': 'Прочее',
                'fields': ['thing_added_date','description'],
            }
        ),
    ]




admin.site.register(Customer, CustomerAdmin)
admin.site.register(Thing, ThingAdmin)
admin.site.register(Order)
