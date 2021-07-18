from django.urls import path
from .views import SuccessfulRegister

urlpatterns = {
    path('register/',SuccessfulRegister.as_view())
}