from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DecimalField

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                null= True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'user_name'

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField(default=0.0)
    image = models.ImageField(null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'product_name'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                     blank=True, null=True, related_name='orders')
    data_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default= False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        if self.customer.name:
            return self.customer.name
        else:
            return 'Customer order'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                     blank=True, null=True,related_name='order_items')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
                     blank=True, null=True, related_name='order_items')
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.product.name:
            return self.product.name
        else:
            return 'Product Name'

    @property        
    def get_total(self):
        total = self.product.price *self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                     blank=True, null=True, related_name='shippling_addresss')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
                     blank=True, null=True,related_name='shippling_addresss')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    date_addred = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.address