from django.urls import path

from  .views import *

urlpatterns=[
 path('', index),
 path('Showcase', showcase, name='Showcase'),
 path('Browse_workers',browse_workers)

]