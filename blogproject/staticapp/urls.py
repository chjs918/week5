from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:blog_id>', detailOne, name ="detailOne"),
    path('newOne/', newOne, name = "newOne"),
    path('createOne/', createOne, name = "createOne"),
    path('editOne/<str:blog_id>', editOne, name = "editOne"),
    path('updateOne/<str:blog_id>', updateOne, name = "updateOne"),
    path('deleteOne/<str:blog_id>', deleteOne, name = "deleteOne"),
]