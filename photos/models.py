from django.db import models
import datetime as dt 
from photos.models import Category

# Create your models here.

class Image(models.Model):
  '''
  Image model to help create new instances of an image object
  '''
  name = models.CharField(max_length=30)
  description = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL)


class Category(models.Model):
  '''
  Category model to create new different category objects
  '''
  name = models.CharField(max_length = 30, null=False, blank=False)

  def __str__(self):
    return self.name 


