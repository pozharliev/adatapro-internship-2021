from django.views.generic import FormView
from api.signUpView.models import Profile


class Login(FormView):
    template_name = "templates/base_login.html"
    form_class = 'Lo'
