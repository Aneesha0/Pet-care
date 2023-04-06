from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='services'),
    path('book/', views.Booking.as_view(), name='book'),
]