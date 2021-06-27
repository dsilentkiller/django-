from django.urls import path
from .views import ListingView, ListingView, SearchView

urlpatterns = [
    path('', ListingView.as_view()),
    path('search', SearchView.as_view()),
    path('title',ListingView.as_view()),
]
