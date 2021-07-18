from django.views.generic import TemplateView


class SuccessfulRegister(TemplateView):
    template_name = 'templates/successful_signup.html'