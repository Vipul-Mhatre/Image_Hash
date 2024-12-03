from django.contrib import admin
from django.urls import path
from .views import upload_image, ImageDataListCreateView, ImageDataDetailView

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('', ImageDataListCreateView.as_view(), name='image_list_create'),
    path('<int:pk>/', ImageDataDetailView.as_view(), name='image_detail'),
]