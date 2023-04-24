from django.urls import path
from .views import *
from .models import Photo
from .views import PhotoDetailView
from django.views.generic.detail import DetailView
from .views import UserDetailView


app_name = 'photo'


urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
    path('list/', PhotoDetailView.as_view(), name='photo_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),


]

