from django.contrib import admin
from .models import Header, Service, Client, LogoClient
# Register your models here.

admin.site.register(Header)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(LogoClient)
