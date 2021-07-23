from django.shortcuts import redirect, render
from django.views import View
from api.helpers.preferences import choose_preference


class SitesView(View):
    template_name = 'templates/sites.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('/login')

    def post(self, request, *args, **kwargs):
        if request['preference'] == 'ardes':
            choose_preference(request, 'want_ardes', 1)
        elif request['preference'] == 'noArdes':
            choose_preference(request, 'want_ardes', 0)
        elif request['preference'] == 'laptop':
            choose_preference(request, 'want_laptop', 1)
        elif request['preference'] == 'noLaptop':
            choose_preference(request, 'want_laptop', 0)