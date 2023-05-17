from django.db import models
from django.contrib.auth.models import User
from client.models import Client
from product.models import Product


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dateOrder = models.DateField()
    TypeOfPaymant = models.CharField(max_length=255)
    class Meta:
        db_table_comment = "Order"
        

class OrderDetails(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField(default=0)
    class Meta:
        db_table_comment = "OrderDetails"
