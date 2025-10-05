from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, MeView, ProfileUpdateView, LogoutView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),   # LOGIN
    path("logout/", LogoutView.as_view(), name="logout"),  # LOGOUT
    path("me/", MeView.as_view(), name="me"),
    path("profile/update/", ProfileUpdateView.as_view(), name="profile_update"),
]
