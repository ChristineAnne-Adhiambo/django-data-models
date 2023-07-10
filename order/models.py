from django.db import models
from payment.models import Payment
from cart.models import Cart
from Customer_system.models import Customer
from shipment.models import Shipment


# Create your models here.

class Order(models.Model):
    shipment = models.ManyToManyField(Shipment)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    payment = models.OneToOneField(Payment,on_delete=models.PROTECT, null= True)
    name = models.CharField(max_length = 16)
    order_number = models.PositiveIntegerField()
    order_total = models.DecimalField(max_digits = 6, decimal_places = 2)
    order_date = models.DateField(auto_now=True)
    location = models.CharField(max_length = 64)
    delivery_choices = (
        ('Pick-Up Point', 'Pick-Up Point'),
        ('Home Delivery', 'Home Delivery'),
    )
    delivery_method = models.CharField(max_length=15, choices=delivery_choices)
    delivery_date = models.DateField()
    
    
    def __str__(self):
        return self.name
    
    
