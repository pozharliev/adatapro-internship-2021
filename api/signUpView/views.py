from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import SignUpForm
from api.helpers.validations import validation
from django.http import JsonResponse


class SignUp(FormView):
    template_name = "templates/base_signup.html"
    form_class = SignUpForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        username = request.POST['profile_username']
        email = request.POST['profile_email']
        password = request.POST['password_hash']
        login_info = SignUpForm(request.POST)
        if validation(username, email, password) and login_info.is_valid():
            login_info.save(commit=True)
            return JsonResponse({'type': 'successful-register'})
        else:
            return JsonResponse({'type': 'unsuccessful-register'})