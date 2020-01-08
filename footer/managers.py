from django.db import models

class DescriptionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(footer__active=True, active=True)

class GeneralInfoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(footer__active=True, active=True)

class SocialNetworkManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(footer__active=True, active=True)

class SubmenuManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(footer__active=True, active=True)


class ButtonManager(models.Manager):
    def filter_actives(self):
        return self.filter(submenu__active=True, active=True)
    