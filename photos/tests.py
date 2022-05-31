from django.test import TestCase
from .models import Image,Category, Location

# Create your tests here.
class CategoryTestClass(TestCase):
  def setUp(self):
        self.genre = Category(name="Fashion")
        self.genre.save_category()

  def test_instance(self):
      self.assertTrue(isinstance(self.genre, Category))

  def test_save_method(self):
      self.genre.save_category()
      category = Category.objects.all()
      self.assertTrue(len(category) > 0)

  def test_delete_method(self):
      self.genre.save_category()
      self.genre.delete_category()
      category = Category.objects.all()
      self.assertTrue(len(category) == 0)

  def test_update(self):
      category = Category.get_category_id(self.genre.id)
      category.update_category('nature')
      category = Category.get_category_id(self.genre.id)
      self.assertTrue(category.name == 'nature')

  
