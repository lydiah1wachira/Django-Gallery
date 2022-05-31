from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def index(request):
  '''
  View function to display the index page and its data 
  '''
  images=Image.get_images()
  locations = Location.objects.all()
  categories = Category.objects.all()
  return render(request, 'index.html', {'images':images, "locations":locations,"categories":categories})

def location_filter(request):
  '''
  View function to display images based on location selected
  '''
  locations = Location.objects.all()
  all_locations = Location.objects.all()
  picked_location = Location.get_location_id(locations)
  images = Image.filter_by_location(locations)
  title = f'{picked_location} Images'
  return render(request, 'main/location.html', {'title':title, 'images':images, 'locations':all_locations, 'location':picked_location,"locations":locations})






def search_results(request):
  locations = Location.objects.all()
  categories = Category.objects.all()
  if 'image' in request.GET and request.GET["image"]:
      search_term = request.GET.get("image")
      searched_images = Image.search_by_category(search_term)
      message = f"{search_term} found "
      
      return render(request, 'main/search.html', {"message":message, "images":searched_images, 'categories': categories, "locations":locations})
  else:
      message = "Please enter a search category"
      return render(request, 'search.html', {"message":message})
  

