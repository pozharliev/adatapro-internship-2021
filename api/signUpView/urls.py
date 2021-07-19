from django.urls import path
from .views import SignUp
from api.signUpView.successfulSignUpView.views import SuccessfulRegister

urlpatterns = [
    path('', SignUp.as_view(), name='signup'),
    path('successful/', SuccessfulRegister.as_view())
]
