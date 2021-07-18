from django.views.generic import FormView
from .forms import SignUpForm


class SignUp(FormView):
    template_name = "templates/base_signup.html"
    form_class = SignUpForm

