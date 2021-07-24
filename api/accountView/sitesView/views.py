from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from api.helpers.preferences import choose_preference


class SitesView(LoginRequiredMixin, TemplateView):
    template_name = 'templates/sites.html'

    # SPAGHETTI CODE WARNING!

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        want_status = {
            True: 0,
            False: 1
        }
        site_name = 'want_{}'.format(request.POST['preference'].replace('no', '').lower())
        selected_preference = want_status[request.POST['preference'].startswith('no')]
        choose_preference(request, site_name, selected_preference)

        return HttpResponseRedirect(reverse_lazy('account:sites'))
