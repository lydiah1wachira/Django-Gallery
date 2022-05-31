from django.urls import re_path,path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  re_path('^$', views.index, name='index'),
  path(r'^search/', views.search_results, name='search_results'),
  path('location/<location>/', views.location_filter, name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


 