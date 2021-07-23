from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from api.helpers.preferences import choose_preference


class SitesView(LoginRequiredMixin, TemplateView):
    template_name = 'templates/sites.html'

    # SPAGHETTI CODE WARNING!

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if request.POST['preference'] == 'ardes':
            choose_preference(request, 'want_ardes', 1)
        elif request.POST['preference'] == 'noArdes':
            choose_preference(request, 'want_ardes', 0)

        elif request.POST['preference'] == 'laptop':
            choose_preference(request, 'want_laptop', 1)
        elif request.POST['preference'] == 'noLaptop':
            choose_preference(request, 'want_laptop', 0)

        elif request.POST['preference'] == 'ozone':
            choose_preference(request, 'want_ozone', 1)
        elif request.POST['preference'] == 'no0zone':
            choose_preference(request, 'want_ozone', 0)

        elif request.POST['preference'] == 'plesio':
            choose_preference(request, 'want_plesio', 1)
        elif request.POST['preference'] == 'noPlesio':
            choose_preference(request, 'want_plesio', 0)

        elif request.POST['preference'] == 'emag':
            choose_preference(request, 'want_emag', 1)
        elif request.POST['preference'] == 'noEmag':
            choose_preference(request, 'want_emag', 0)

        elif request.POST['preference'] == 'also':
            choose_preference(request, 'want_also', 1)
        elif request.POST['preference'] == 'noAlso':
            choose_preference(request, 'want_also', 0)

        elif request.POST['preference'] == 'jarcomputers':
            choose_preference(request, 'want_jar', 1)
        elif request.POST['preference'] == 'noJarcomputers':
            choose_preference(request, 'want_jar', 0)

        elif request.POST['preference'] == 'polycomp':
            choose_preference(request, 'want_polycomp', 1)
        else:
            choose_preference(request, 'want_polycomp', 0)


