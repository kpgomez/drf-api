from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Toy(models.Model):
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cost_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    # item_no = models.CharField(max_length=32)
    # sku = models.CharField(max_length=32)
    # asin = models.CharField(max_length=10)
    # manufacturer = models.CharField(max_length=20)
    # distributor = models.CharField(max_length=20)

    def __str__(self):
        return self.title
