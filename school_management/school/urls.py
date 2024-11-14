from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, StudentViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'classes', ClassViewSet, basename='class')  # Route for the 'classes' endpoint
router.register(r'students', StudentViewSet, basename='student')  # Route for the 'students' endpoint

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),  # Include all the router URLs
]
