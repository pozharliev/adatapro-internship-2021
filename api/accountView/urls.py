from django.urls import path
from api.accountView.views import AccountView

urlpatterns = [
    path('', AccountView.as_view() )
]