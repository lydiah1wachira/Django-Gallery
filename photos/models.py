
from django.db import models



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
  photo = models.ImageField(upload_to = 'gallery_images/', null=True, blank=False)
  pub_date = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

  def __str__(self):
      return self.description

  def save_image(self):
      self.save()

  def delete_image(self):
      self.delete()

  @classmethod
  def update_image(cls,id, photo,name, description, location, category):
      update = cls.objects.filter(id = id).update( image_name=name, description=description, location=location, category=category)
      return update
      
  @classmethod
  def get_images(cls):
      images = cls.objects.all()
      return images
    
  @classmethod
  def search_by_category(cls, search_term):
      images = cls.objects.filter(category__title__icontains=search_term)
      return images
    
  @classmethod
  def get_image_by_id(cls,id):
      image = cls.objects.filter(id= id).all()
      return image
    
  @classmethod
  def filter_by_location(cls, img_location):
      images_location = cls.objects.filter(location__id=img_location)
      return images_location



