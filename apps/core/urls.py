from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('photos/', views.photos, name='photos'),
    path('ml-crush-details/', views.ml_crush_details, name='ml_crush_details'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('api/test/', views.test_api, name='test_api'),
] 