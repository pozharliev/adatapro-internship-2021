from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.models import User
from api.helpers.validations import validation
from django.http import JsonResponse

from api.signUpView.forms import SignUpForm


class SignUp(FormView):
    template_name = "templates/base_signup.html"
    form_class = SignUpForm
    success_url = 'successful'

    def post(self, request, *args, **kwargs):
        redirection = super(SignUp, self).post(self, request, args, kwargs)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if validation(username, email, password):
            try:
                user = User.objects.create_user(username, email, password)
                return redirection
            except IntegrityError:
                return render(request, 'templates/taken.html', {'form': SignUpForm})
        else:
            return render(request, 'templates/invalid_signup.html', {'form': SignUpForm} )

