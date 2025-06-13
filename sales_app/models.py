from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newletter_abo = models.BooleanField(default=False)
    email_adress = models.CharField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=9.99)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    # pass

