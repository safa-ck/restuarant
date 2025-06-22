from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    item = models.TextField()
    image =models.FileField(upload_to="category")

class Dish(models.Model):
    title = models.CharField(max_length=255)
    Description = models.TextField()
    image = models.FileField(upload_to="dish")    
    

# Create your models here.
