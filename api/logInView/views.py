from django.views.generic import TemplateView


class Login(TemplateView):
    template_name = "templates/base_login.html"
