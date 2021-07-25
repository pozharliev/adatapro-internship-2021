from django.views.generic import FormView, TemplateView


class DeleteAccountView(TemplateView):
    template_name = 'templates/account_options/delete.html'