from django.urls import path
from .views import post, put, delete, get

urlpatterns = [
 path('', get, name='get'),
 path('post/', post, name='post'),
 path('put/<int:pk>/', put, name='put'),
 path('delete/<int:pk>/', delete, name='delete')


 ]