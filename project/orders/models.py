from django.db import models

class SalesOrder(models.Model):
    amount = models.IntegerFieldde
    description = models.CharField(max_length=255)