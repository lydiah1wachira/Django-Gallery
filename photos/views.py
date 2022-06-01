
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def index(request):
  '''
  View function to display the index page and its data 
  '''

  locations = Location.objects.all()
  categories = Category.objects.all()
  return render(request, 'index.html', { "locations":locations,"categories":categories})


def gallery(request):
  images = Image.get_images()
  locations = Location.objects.all()
  categories = Category.objects.all()
  return render(request, 'gallery.html', {"images":images,"locations":locations, "categories":categories })




def search_results(request):
  locations = Location.objects.all()
  categories = Category.objects.all()

  if 'searchedImage' in request.GET and request.GET["searchedImage"]:
      search_term = request.GET.get("searchedImage")
      searched_images = Image.search_by_category(search_term)
      message = f"{search_term} "
      
      return render(request, 'search.html', {"message":message, "images":searched_images, 'categories': categories, "locations":locations})
  else:
      message = "Please enter a search category"
      return render(request, 'search.html', {"message":message})
  

def location_filter(request, location_id):
  '''
  View function to display images based on location selected
  '''
  locations = Location.objects.all()
  categories = Category.objects.all()

  try:
    showLocations = Image.filter_by_location(location_id)

  except Image.DoesNotExist:
    raise Http404()

  return render(request, 'location.html', {"locations":locations,
  "categories":categories, "showLocations":showLocations})

def display_image(request, image_id):
  locations = Location.objects.all()
  categories = Category.objects.all()

  try:
    display_image = Image.objects.get(id = image_id)
  
  except Image.DoesNotExist:
    raise Http404

  return render(request, 'detailed-image', {"locations":locations, "categories":categories,"display_image":display_image})

