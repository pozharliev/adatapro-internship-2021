from django.forms import ModelForm
from .models import Profile
from django import forms


class SignUpForm(ModelForm):
    profile_username = forms.CharField(label="Потребителско име", max_length=64, widget=forms.TextInput(attrs={'class': 'input '
                                                                                                               'mr',
                                                                                                               'placeholder': 'Mitko123 '
                                                                                                               }))
    profile_email = forms.EmailField(label="Email", max_length=128, widget=forms.EmailInput(attrs={'class': 'input mr',
                                                                                                   'placeholder': 'mitko123@adatapro.bg '
                                                                                                   }))
    password_hash = forms.CharField(label='Парола', max_length=256, widget=forms.PasswordInput({'class': 'input mr',
                                                                                                'placeholder': '********',
                                                                                                }))

    class Meta:
        model = Profile
        fields = ["profile_username", "profile_email", "password_hash"]
