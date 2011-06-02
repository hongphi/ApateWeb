from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'image')
    details = models.TextField()
    point = models.SmallIntegerField()
    price = models.IntegerField()
    tags = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.product_name
    
class Vote(models.Model):
    vote_point = models.IntegerField()
    vote_user = models.ForeignKey(User)
    vote_product = models.ForeignKey(Product)
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key = True)
    comment_content = models.TextField()
    comment_date = models.DateTimeField(auto_now = True)
    comment_product = models.ForeignKey(Product)
    comment_user = models.ForeignKey(User)
    



