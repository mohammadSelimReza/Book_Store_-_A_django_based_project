from django.urls import path
from .views import UserRegistrationView,UserLoginView,UserLogoutView,UserProfileUpdate

urlpatterns = [
    path('registration/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(), name='logout'),
    path('update/',UserProfileUpdate.as_view(),name='update'),
]
