from django.db import models

# Create your models here.

from category.models import Category
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=['name']),
                   models.Index(fields=['price'])
                   ]


    def __str__(self):
        return self.name