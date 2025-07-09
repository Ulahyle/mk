from django.contrib import admin
from store.models import Customer, Address, Product, Discount, Order, OrderItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number')
    search_fields = ('name', 'email')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'street', 'city')
    search_fields = ('customer__name', 'city')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('stock',)

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'percentage', 'active')
    list_filter = ('active',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at', 'discount')
    list_filter = ('created_at',)
    search_fields = ('customer__name',)

@admin.register(OrderItem)
class OredrItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')