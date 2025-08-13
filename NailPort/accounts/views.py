from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import get_user_model

from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from NailPort.accounts.models import Profile
from NailPort.accounts.forms import ProfileUpdateForm

UserModel = get_user_model()


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')  # ще го направим по-късно

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # автоматично логване
        return response


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user.profile


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'          # ще създадем този шаблон
    redirect_authenticated_user = True             # ако вече е логнат – пренасочва
    next_page = reverse_lazy('home')               # накъде след успешен login


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home')               # накъде след logout
