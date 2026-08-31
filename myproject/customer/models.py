from django.db import models

# Create your models here.

class Customers (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,
                              db_index=True)

    def __str__(self):
        return self.name

    
