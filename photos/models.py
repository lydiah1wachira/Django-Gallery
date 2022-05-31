from unicodedata import category
from django.db import models
import datetime as dt 


# Create your models here.


class Category(models.Model):
  '''
  Category model to create new different category objects
  '''
  name = models.CharField(max_length = 30, null=False, blank=False)

  def __str__(self):
    return self.name 

  def save_category(self):
    self.save()

  def update_category(self, update):
    self.name = update 
    self.save()

  def delete_category(self):
        self.delete()

  @classmethod
  def get_category_id(cls, id):
    category = Category.objects.get(pk = id)
    return category




class Location(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name 


  def save_location(self):
    self.save()

  def update_location(self, update):
    self.name = update
    self.save()

  @classmethod
  def get_locations(cls, id):
    locations = Location.objects.all(pk = id)
    return locations




class Image(models.Model):
  '''
  Image model to help create new instances of an image object
  '''
  name = models.CharField(max_length=30)
  description = models.TextField()
  photo = models.ImageField(null=False, blank=False)
  pub_date = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.description


