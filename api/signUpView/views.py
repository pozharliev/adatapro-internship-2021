from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import SignUpForm


class SignUp(FormView):
    template_name = "templates/base_signup.html"
    form_class = SignUpForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        login = super(SignUp, self).post(self, request, *args, **kwargs)
        username = request.POST['profile_username']
        email = request.POST['profile_email']
        password = request.POST['password_hash']
        print(username, email, password)
        login_info = SignUpForm(data=request.POST)

        if SignUpForm.form_validation(username, email, password):
            login_info.save(commit=True)
            return login
        else:
            return redirect('/')