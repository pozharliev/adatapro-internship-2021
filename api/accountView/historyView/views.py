from django.views.generic import ListView
from api.accountView.historyView.models import HistoryScraping


class HistoryView(ListView):
    template_name = 'templates/history.html'
    model = HistoryScraping
    paginate_by = 5
