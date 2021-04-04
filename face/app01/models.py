from django.db import models


# Create your models here.
class user_native(models.Model):
    uid = models.FloatField()
    name = models.CharField(max_length=64)
    data = models.CharField(max_length=64)


class user_part(models.Model):
    uid = models.FloatField()
    name = models.CharField(max_length=64)
    data = models.CharField(max_length=64)
    p = models.CharField(max_length=64)
