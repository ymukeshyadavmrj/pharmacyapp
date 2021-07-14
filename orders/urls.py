from django.urls import path,include
from orders import views


urlpatterns = [
    path('orders/<pk>',views.ordersapi),
    path('orders/',views.ordersapi),
]
