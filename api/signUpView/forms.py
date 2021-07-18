from django.forms import ModelForm
from .models import Profile


class SignUpForm(ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            "profile_username" : "Username",
            "profile_email" : "Email",
            "password_hash" : "Password"
        }