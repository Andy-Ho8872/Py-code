from django.db import models

# Create your models(DB) here.

class Product(models.Model):
    name = models.CharField(max_length=255)  #define the max_length of the title or the content
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083) #fixed length
    
class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()