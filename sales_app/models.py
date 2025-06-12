from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # newletter_abo = models.BooleanField()
    # email_adress = models.EmailField()
    # account = models.FloatField()