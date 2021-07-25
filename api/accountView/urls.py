from django.urls import path
from api.accountView.historyView.views import HistoryView
from api.accountView.sitesView.views import SitesView
from api.accountView.usersView.views import UsersView
from api.accountView.views import AccountView
from api.changeEmailView.views import ChangeEmailView
from api.changePasswordView.views import ChangePasswordView
from api.deleteAccountView.views import DeleteAccountView

app_name = 'account'

urlpatterns = [
    path('', AccountView.as_view()),
    path('sites/', SitesView.as_view(), name='sites'),
    path('history/', HistoryView.as_view()),
    path('users/', UsersView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('change-email/', ChangeEmailView.as_view()),
    path('delete-account/', DeleteAccountView.as_view())
]
