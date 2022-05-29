from django.db import models
import datetime as dt 

# Create your models here.
class Image(models.Model):
  '''
  Image model to help create new instances of an image object
  '''
  name = models.CharField(max_length=30)
  description = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)


