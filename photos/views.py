from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  '''
  View function to display the index page and its data 
  '''
  return render(request, 'index.html')


# def all_photos(request):
#   '''
#   view function to display the photos gallery page.
#   '''
#   return render(request, 'all-photos.html')