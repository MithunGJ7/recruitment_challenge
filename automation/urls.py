from django.urls import path
from .views import execute_tests

# Define the URL patterns for the application(automation app)
urlpatterns = [
    # Endpoint for executing tests
    # Function based View
    path('tests/v1/execute', execute_tests, name='execute_tests'),
]
