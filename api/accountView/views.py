from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'templates/account.html'

