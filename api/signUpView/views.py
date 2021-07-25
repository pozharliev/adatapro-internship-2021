from django.db import IntegrityError
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.models import User
from api.helpers.validations import validation
from ..accountView.models import ProfilePreferences
from django.core.mail import send_mail
from api.signUpView.forms import SignUpForm
from ..settings import EMAIL_HOST_USER


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
                preferences = ProfilePreferences(profile_username=user)
                preferences.save()
                send_mail(
                    'Subject here',
                    'Here is the message.',
                    EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return redirection
            except IntegrityError:
                return render(request, 'templates/taken.html', {'form': SignUpForm})
        else:
            return render(request, 'templates/invalid_signup.html', {'form': SignUpForm})
