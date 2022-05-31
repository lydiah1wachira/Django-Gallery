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


class LocationTestCLass(TestCase):
   
  def setUp(self):
      self.locale = Location(name="Kenya")
      self.locale.save_location()

  def test_instance(self):
      self.assertTrue(isinstance(self.locale,Location))

  def test_save_method(self):
      self.locale.save_location()
      locations = Location.objects.all()
      self.assertTrue(len(locations) > 0)

  def test_delete_method(self):
      self.locale.save_location()
      self.locale.delete_location()
      location = Location.objects.all()
      self.assertTrue(len(location) == 0)

  def test_update(self):
      location = Location.get_location_id(self.locale.id)
      location.update_location('Msituni')
      location = Location.get_location_id(self.locale.id)
      self.assertTrue(location.name == 'Msituni')


class ImageTestClass(TestCase):
    
    def setUp(self):
        self.genre = Category(name="photography")
        self.genre.save_category()

        self.locale = Location(name="Msituni")
        self.locale.save_location()

        self.image = Image(name='image test', description='image test take 1',location=self.locale, category=self.genre)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.genre.delete_category()
        self.locale.delete_location()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)


    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_by_category(self):
        images = Image.search_by_category('photography')
        self.assertTrue(len(images)>0)

    def test_filter_by_location(self):
        images = Image.filter_by_location('1')
        print(images)
        self.assertTrue(len(images)>0)

    def test_update_image(self):
        self.image.save_image()
        image = Image.update_image( self.image.id, 'test update', 'my test',self.locale, self.genre)
        upimage = Image.objects.filter(id = self.image.id)
        print(upimage)
        self.assertTrue(Image.name == 'test update')

