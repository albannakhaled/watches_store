from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    quantity_in_stock = models.IntegerField(default=0)
    category = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table_comment = "Product"