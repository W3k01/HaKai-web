from django.shortcuts import render, redirect
from django.http import JsonResponse


def home(request):
    """Main home page view"""
    return render(request, 'main.html')


def events(request):
    """Events page view"""
    return render(request, 'core/events.html')


def photos(request):
    """Photos page view"""
    return render(request, 'core/photos.html')


def ml_crush_details(request):
    """ML Crush details page view"""
    return render(request, 'core/ml-crush-details.html')


def break_the_code_details(request):
    """Break the Code details page view"""
    return render(request, 'core/break-the-code-details.html')


def website_majesty_details(request):
    """Website Majesty details page view"""
    return render(request, 'core/website-majesty-details.html')


def app_grinding_details(request):
    """App Grinding details page view"""
    return render(request, 'core/app-grinding-details.html')


def register(request):
    """Registration redirect to events page"""
    return redirect('core:events')


def profile(request):
    """User profile page view"""
    return render(request, 'core/profile.html')


def test_api(request):
    return JsonResponse({"message": "Hello from Django API!"})
