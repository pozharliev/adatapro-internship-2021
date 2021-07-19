from django.views.generic import FormView
from api.logInView.forms import LoginForm


class Login(FormView):
    template_name = "templates/base_login.html"
    form_class = LoginForm
    success_url = '/'
