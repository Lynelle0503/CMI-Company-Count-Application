from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', uploadFile, name = "Upload Page"),
    path('query-builder/', qbPage, name = "Query Builder Page"),
]
