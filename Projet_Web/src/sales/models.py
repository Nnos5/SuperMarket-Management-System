from django.db import models
from accounts.models import User
from stocks.models import Product

class Sales(models.Model):
    name = models.CharField(max_length=50)
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.FloatField(verbose_name='unit price')
    total_amount = models.PositiveIntegerField(verbose_name='total amount')
    status = models.CharField(max_length=50, default='pending')
    sold_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    sold_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        """Returns a string representation of this sale."""
        return self.name
