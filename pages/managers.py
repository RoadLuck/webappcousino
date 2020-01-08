from django.db import models

class PageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(avtive=True)