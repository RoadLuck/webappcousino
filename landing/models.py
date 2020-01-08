from django.db import models

# Create your models here.

class Header(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    ROW = [('1','Row 1'), ('2', 'Row 2'), ('3','Row 3')]

    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=60, null=True)
    row = models.CharField(max_length=1, null=True, choices=ROW, default='1')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=120) #Despues esto se cambia a una relacion con User o una app opinion
    opinion = models.TextField()
    image = models.ImageField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class LogoClient(models.Model):
    image = models.ImageField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Logo"



