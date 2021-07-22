from django.db import models
import datetime


class TodoItem(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    completed = models.BooleanField(null=True, blank=True, default=False)
    url = models.CharField(max_length=256, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(
        default=datetime.datetime.now, editable=False, blank=True, null=True)

    class Meta:
        ordering = ['order']
