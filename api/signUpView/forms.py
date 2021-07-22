from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(ModelForm):
    username = forms.CharField(label="Потребителско име", max_length=64,
                               widget=forms.TextInput(attrs={'class': 'input mr',
                                                             'placeholder': 'Mitko123 '}))
    email = forms.EmailField(label="Email", max_length=128,
                             widget=forms.EmailInput(attrs={'class': 'input mr',
                                                            'placeholder': 'mitko123@adatapro.bg '
                                                            }))
    password = forms.CharField(label='Парола', max_length=256,
                               widget=forms.PasswordInput({'class': 'input mr',
                                                           'placeholder': '********',
                                                           }))

    class Meta:
        model = User
        fields = ["username", "email", "password"]
