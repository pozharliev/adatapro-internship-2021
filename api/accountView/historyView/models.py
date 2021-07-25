from django.db import models


class HistoryScraping(models.Model):
    site = models.CharField(max_length=256)
    price = models.FloatField(max_length=32)
    date = models.DateField(auto_now=True)
    site_link = models.URLField(max_length=512)

    class Meta:
        managed = True
