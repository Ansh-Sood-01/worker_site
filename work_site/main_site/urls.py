from django.urls import path

from  .views import *

urlpatterns=[
 path('', index),
 path('Showcase', showcase, name='Showcase'),

]