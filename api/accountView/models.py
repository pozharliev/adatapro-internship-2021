from django.contrib.auth.models import User
from django.db import models


class ProfilePreferences(models.Model):
    profile_username = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    want_laptop = models.BooleanField(default=True)
    want_polycomp = models.BooleanField(default=True)
    want_jar = models.BooleanField(default=True)
    want_also = models.BooleanField(default=True)
    want_ardes = models.BooleanField(default=True)
    want_ozone = models.BooleanField(default=True)
    want_emag = models.BooleanField(default=True)
    want_plesio = models.BooleanField(default=True)

    class Meta:
        managed = True
