from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'image')
    details = models.TextField()
    point = models.SmallIntegerField()
    price = models.IntegerField()
    tags = models.SmallIntegerField()



