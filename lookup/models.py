from django.db import models


class Restaurants(models.Model):
    name = models.CharField(max_length=20)
    dinner_for_two = models.FloatField()
    rating = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class CustomerInfo(models.Model):
    customer_fname = models.CharField(max_length=30)
    customer_lname = models.CharField(max_length=30)
    customer_phone = models.IntegerField(max_length=12)

