from django.shortcuts import redirect
from django.views.generic import TemplateView


class AccountView(TemplateView):
    template_name = 'templates/account.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(AccountView, self).get(self,request, *args, **kwargs)
        else:
            return redirect('/login')