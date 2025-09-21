from django.db import models

class OrderStatus(models.Model):
    name= models.CharField(max_length=50,unique=True)

class Order(models.Model):
    status = models.ForeignKey(
        'OrderStatus',
        on_delete = models.SET_NULL,
        null = True,
        blank= True,
        related_name='orders'
    )
