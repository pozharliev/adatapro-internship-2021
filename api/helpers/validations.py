import re


def validation(username, email, password):
    username_regex = '/^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$/'
    email_regex = '/(([a-z]+)([._a-z0-9])([a-z0-9]+)).{1,64}(@)([a-z]+)([.a-z])([a-z])+/gmi'
    password_regex = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    if re.match(username_regex, username) and re.match(email_regex, email) and re.match(password_regex, password):
        return True

    else:
        return False
