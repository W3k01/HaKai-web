from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def home(request):
    """Main home page view"""
    return render(request, 'main.html')


def events(request):
    """Events page view"""
    return render(request, 'events.html')


def photos(request):
    """Photos page view"""
    return render(request, 'photos.html')


def ml_crush_details(request):
    """ML Crush details page view"""
    return render(request, 'ml-crush-details.html')


def register(request):
    """Registration redirect to events page"""
    return redirect('main:events')


def test_api(request):
    return JsonResponse({"message": "Hello from Django API!"})
