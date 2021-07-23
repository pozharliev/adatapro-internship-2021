from django.urls import path
from api.accountView.sitesView.views import SitesView
from api.accountView.views import AccountView

urlpatterns = [
    path('', AccountView.as_view()),
    path('sites/', SitesView.as_view())
]