from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['User', 'name',
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
    list_display = ['user', 'customer',
                    'product', 'quantity', 'ordered_date', 'status']
    list_filter = ('user','status','product')
    search_fields = ('quantity','ordered_date')
    list_per_page = 10
    list_editable =('status',)
