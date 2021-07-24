from django.urls import path
from api.accountView.historyView.views import HistoryView
from api.accountView.sitesView.views import SitesView
from api.accountView.usersView.views import UsersView
from api.accountView.views import AccountView

urlpatterns = [
    path('', AccountView.as_view()),
    path('sites/', SitesView.as_view()),
    path('history/', HistoryView.as_view()),
    path('users/', UsersView.as_view()),
]
