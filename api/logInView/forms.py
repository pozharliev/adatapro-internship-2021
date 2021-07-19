from django.forms import ModelForm
from api.signUpView.models import Profile
from django import forms


class LoginForm(ModelForm):
    profile_username = forms.CharField(label="Потребителско име", max_length=64, widget=forms.TextInput())
    password_hash = forms.CharField(label='Парола', max_length=256, widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['profile_username', 'password_hash']