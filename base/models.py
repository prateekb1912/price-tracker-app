from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 300, null=False)
    # description = models.TextField(null = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    avaialable = models.BinaryField()
    last_update = models.DateTimeField(auto_now = True)
