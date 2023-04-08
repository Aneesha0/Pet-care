# accounts/urls.py
from django.urls import path

from .views import SignUpView
from . import views

app_name = 'accounts'
urlpatterns = [
    path("",views.account.as_view(), name="account"),
    path("default/", views.Update.as_view(), name="default"),
    path("display/",views.Display.as_view(), name="display"),
    path("<int:counter>/cancel/",views.Cancel.as_view(), name="cancel"),
    path("signup/", SignUpView.as_view(), name="signup"),
]