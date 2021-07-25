from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Потребителско име", max_length=64,
                               widget=forms.TextInput(attrs={'class': 'input mr',
                                                             'placeholder': 'Mitko123'}))
    password = forms.CharField(label='Парола', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'input mr',
                                                                 'placeholder': '********'}))

    class Meta:
        fields = ['username', 'password']
