from django.views.generic import ListView
from api.accountView.historyView.models import HistoryScraping
from api.accountView.models import ProfilePreferences
import operator
from functools import reduce
from django.db.models import Q


class AccountView(ListView):
    template_name = 'templates/account.html'
    model = HistoryScraping
    paginate_by = 5
    # ordering =

    @property
    def get_filter_terms(self):
        profile_preferences = ProfilePreferences.objects.get(profile_username=self.request.user)
        site_names = [k.split('_')[-1] for k, v in profile_preferences.__dict__.items() if v and k.startswith('want')]
        filter_terms = [Q(**{'site__icontains': site_name}) for site_name in site_names]

        return filter_terms

    def get_queryset(self, ):
        queryset = super(AccountView, self).get_queryset()

        return queryset.filter(reduce(operator.or_, self.get_filter_terms))
