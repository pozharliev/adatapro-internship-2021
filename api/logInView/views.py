from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView
from api.logInView.forms import LoginForm
from django.contrib.auth import authenticate, login


class Login(FormView):
    template_name = "templates/base_login.html"
    form_class = LoginForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        login_credentials = super(Login, self).post(self, request, *args, **kwargs)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return login_credentials
        else:
            return render(request, 'templates/invalid_login.html', {'form': LoginForm})
