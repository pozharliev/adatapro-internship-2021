from django.views.generic import ListView
from api.accountView.historyView.models import HistoryScraping
from api.accountView.models import ProfilePreferences


class HistoryView(ListView):
    template_name = 'templates/history.html'
    model = HistoryScraping
    paginate_by = 5

    def get_queryset(self,):
        query = super(HistoryView, self).get_queryset()
        preferences = {
            'Ardes': None,
            'Ozone': None,
            'Laptop': None,
            'Polycomp': None,
            'Jar': None,
            'Also': None,
            'Emag': None,
            'Plesio': None
        }
        for p in ProfilePreferences.objects.raw(f"""
        SELECT id, want_laptop, want_polycomp, want_jar, want_also, want_ardes, want_ozone, want_emag, want_plesio
        FROM accountview_profilepreferences
        WHERE profile_username_id = {self.request.user.id}
        """):
            preferences['Ardes'] = p.want_ardes
            preferences['Ozone'] = p.want_ozone
            preferences['Laptop'] = p.want_laptop
            preferences['Polycomp'] = p.want_polycomp
            preferences['Jar'] = p.want_jar
            preferences['Also'] = p.want_also
            preferences['Emag'] = p.want_emag
            preferences['Plesio'] = p.want_plesio
        return query
