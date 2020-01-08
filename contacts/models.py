from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=9)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name