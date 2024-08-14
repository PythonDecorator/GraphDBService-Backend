"""
Core views for app.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    """Welcome to GraphDB Service APIs. Please see our documentations for more information on
    how to use the API."""
    return Response({'ok': True, "message": "Welcome To GraphDB Service APIs"})


@api_view(['GET'])
def health_check(request):
    """Returns successful response."""
    return Response({'healthy': True})
