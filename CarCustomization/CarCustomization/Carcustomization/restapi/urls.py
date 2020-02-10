from django.urls import path
from .views import *

urlpatterns = [
    path('customer/',view_get_post_customerList),
    path('customer/<int:ID>',view_getByID_updateByID_deleteByID),
]