from django.urls import path

from . import views
from rest_framework import routers
from django.urls import path, include, re_path
# Rename views to avoid conflict with app views
from rest_framework.authtoken import views as rest_views

"""
When using viewsets instead of views, we can automatically generate the URL conf for our API, by simply registering the viewsets with a router class.

If we need more control over the API URLs we can simply drop down to using regular class-based views (APIViews), and writing the URL conf explicitly.
"""

router = routers.DefaultRouter()

# Rename views to avoid conflict with app views
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    # URLs for class-based views (Generics, APIViews)
    # http://localhost:8000/todo/
    # http://localhost:8000/todo/<int:pk>

]

