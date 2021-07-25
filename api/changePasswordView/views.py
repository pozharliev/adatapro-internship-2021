from django.views.generic import FormView, TemplateView


class ChangePasswordView(TemplateView):
    template_name = 'templates/account_options/new_password.html'