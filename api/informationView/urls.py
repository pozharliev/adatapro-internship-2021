from django.urls import path
from api.informationView.views import InformationView

urlpatterns = [
    path('', InformationView.as_view())
]