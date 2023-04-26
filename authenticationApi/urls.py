from django.urls import path
from .views import  UserRegistrationView, UserLoginView, UserProfileView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("get-profile/", UserProfileView.as_view(), name="profile"),

]
