from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('photos/', views.photos, name='photos'),
    path('ml-crush-details/', views.ml_crush_details, name='ml_crush_details'),
    path('break-the-code-details/', views.break_the_code_details, name='break_the_code_details'),
    path('website-majesty-details/', views.website_majesty_details, name='website_majesty_details'),
    path('app-grinding-details/', views.app_grinding_details, name='app_grinding_details'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('api/test/', views.test_api, name='test_api'),
] 