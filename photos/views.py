from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def index(request):
  '''
  View function to display the index page and its data 
  '''
  return render(request, 'index.html')


def search_results(request):
  '''
  View function to display the images based on category serached
  '''
  if 'search' in request.GET and request.GET["search"]:
    category = request.GET.get('search')
    category_images= Image.search_by_category(category)
    message = f'{category} images:'
    print(category_images)

    return render(request, 'search.html', {"message": message, "images": category_images})
  
  else:
    message = "The category was not found"
    return render(request, 'search.html', {"message":message})

