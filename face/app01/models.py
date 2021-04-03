from django.db import models


# Create your models here.
class user(models.Model):
    uid = models.FloatField()
    name = models.CharField(max_length=32)
    data = models.CharField(max_length=32)
