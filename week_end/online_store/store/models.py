from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='adresses')
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.street}, {self.city}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Discount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    percentage = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.percentage}%"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"order #{self.id} - {self.customer.name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"