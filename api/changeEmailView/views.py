from django.views.generic import FormView, TemplateView


class ChangeEmailView(TemplateView):
    template_name = 'templates/account_options/new_email.html'