from django.urls import re_path,path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  re_path('^$', views.index, name='index'),
  path('gallery/', views.gallery, name='gallery'),
  path('search/', views.search_results, name='search_results'),
  path('location/<location>/', views.location_filter, name='location'),
  re_path('detailed-image/<image_id>/', views.display_image, name ='detailed-image')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


 