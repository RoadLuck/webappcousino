from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Footer)
class FooterAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Description)
class DescriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    pass

@admin.register(models.SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ButtonSubmenu)
class ButtonSubMenuAdmin(admin.ModelAdmin):
    pass
