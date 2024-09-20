from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', uploadFile, name = "Upload_Page"),
    path('query-builder/', qbPage, name = "Query_Builder_Page"),
]
