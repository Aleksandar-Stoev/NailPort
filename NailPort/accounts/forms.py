from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from NailPort.accounts.models import Profile

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone_number', 'profile_image')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
        }
