from django.urls import path
from NailPort.accounts.views import RegisterView, ProfileUpdateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
