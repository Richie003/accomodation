from django.urls import path
from appauth import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signup_api/', views.signup_api, name="signup_api"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout")
]