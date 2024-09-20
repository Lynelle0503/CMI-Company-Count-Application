from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', uploadFile, name = "Upload_Page"),
    path('model/delete/', modelDelete, name = "Delete_model"),
]
