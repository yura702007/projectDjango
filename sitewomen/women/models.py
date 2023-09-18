from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.TimeField(auto_now_add=True)
    time_update = models.TimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
