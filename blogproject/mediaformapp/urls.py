from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detailTwo/<str:blog_id>', detailTwo, name ="detailTwo"),
    path('newTwo/', newTwo, name = "newTwo"),
    path('editTwo/<str:blog_id>', editTwo, name = "editTwo"),
    path('deleteTwo/<str:blog_id>', deleteTwo, name = "deleteTwo")
]