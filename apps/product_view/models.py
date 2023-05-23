from django.db import models

# Create your models here.
class Product(models.Model):
    item_name = models.CharField(max_length=30, default='')
    total_amount = models.IntegerField(default='')
    available = models.IntegerField()
    on_order = models.IntegerField()

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self) -> str:
        return self.item_name

class ActiveOrder(models.Model):
    order_name = models.CharField(max_length=100, null=True, default="")
    order_location = models.CharField(max_length=200, null=True, default="")
    order_data = models.TextField()

    def __str__(self) -> str:
        return self.order_name
