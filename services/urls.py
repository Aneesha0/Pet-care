from django.urls import path

from . import views

app_name = 'services'
urlpatterns = [
    path('', views.Index.as_view(), name='services'),
    path('<int:service_id>/book/', views.Booking.as_view(), name='book'),
]