from django.urls import path
from NailPort.core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
