from django.db import models

# Create your models here.
from customer.models import Customers
from product.models import Product



class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        Orders,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    