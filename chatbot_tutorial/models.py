from django.db import models
from django.utils import timezone


class Logs(models.Model):
    user = models.CharField(max_length=50, null=False, unique=True, blank=False)
    stupid_count = models.IntegerField(default=0)
    fat_count = models.IntegerField(default=0)
    dumb_count = models.IntegerField(default=0)
    created_on = models.DateTimeField(editable=False, null=False, blank=False)

    def save(self, *args, **kwargs):
        """ On save, update timestamps, better than auto_now_add"""
        if not self.pk:
            self.created_on = timezone.now()
        return super(Logs, self).save(*args, **kwargs)
