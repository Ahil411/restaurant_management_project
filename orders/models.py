from django.db import models

class OrderStatus(models.Model):
    name= models.Charafield(max_length=50,unique=True)

    def __str__(self):
        return self.name
class Order(models.Model):
    status = models.ForeignKey(
        'OrderStatus',
        on_delete = models.SET_NULL,
        null = True,
        blank= True,
        related_name='orders'
    )
