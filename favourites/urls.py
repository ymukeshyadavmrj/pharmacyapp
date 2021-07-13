from django.urls import path,include
from favourites import views


urlpatterns = [
    path('favourites/<pk>',views.favouritesapi),
]
