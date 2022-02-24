from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 300, null=False)
    slug = models.SlugField(null=True)
    # description = models.TextField(null = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    avaialable = models.BinaryField()
    last_update = models.DateTimeField(auto_now = True)

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique = True)
    # phone = models.BigIntegerField()
    # birth_date = models.DateField(null = True)

class WatchList(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_created = True)
    last_updated = models.DateTimeField(auto_now = True)
    products = models.ManyToManyField(Product, related_name='lists')