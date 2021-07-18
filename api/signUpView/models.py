from django.db import models


class Profile(models.Model):
    profile_id = models.BigAutoField(primary_key=True)
    profile_username = models.CharField(max_length=64, unique=True)
    profile_email = models.EmailField(max_length=128, unique=True)
    password_hash = models.CharField(max_length=256)

    class Meta:
        managed = True
