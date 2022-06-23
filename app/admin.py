from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced,
    Verification,
    Brand,
)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id','category')
#     list_filter = ('category',)
#     search_fields = ('category',)
#     ordering = ('category',)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['User', 'id', 'name',
                    'locality', 'city', 'zipcode', 'state']
    list_filter = ('User','state')
    search_fields = ('name','locality','city','zipcode')
    list_per_page = 8

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'selling_price', 'discounted_prie', 'short_description',
                    'description', 'brand', 'category', 'product_image']
    list_filter =('brand','category')
    search_fields =('title','selling_price','discounted_prie','description')
    list_per_page = 6

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']
    list_filter =('user','product')
    search_fields =('quantity',)
    list_per_page = 9

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'customer', 'customer_info',
                    'product', 'product_info', 'quantity', 'ordered_date', 'status']
    list_filter = ('user','status','product')
    search_fields = ('quantity','ordered_date')
    list_per_page = 10
    list_editable =('status',)

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)
    
    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin,):
	list_display = ['id', 'token','user', 'verify']
    