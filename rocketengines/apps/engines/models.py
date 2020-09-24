from django.db import models
from registration.models import User

class Category(models.Model):
    cat_name = models.CharField('category', max_length = 100)

class Product(models.Model):
    category = models.ForeignKey(Category)
    product_name = models.CharField('product_name', max_length = 100)
    product_description = models.TextField('product_description')
    product_rating = models.IntegerField('product_rating')


# Create your models here.
