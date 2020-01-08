
from django.db import models
from . import managers

# Create your models here.
class Footer(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

        

class Description(models.Model):
    footer = models.OneToOneField(Footer, on_delete=models.CASCADE, related_name='footer')
    logo = models.ImageField()
    description = models.TextField()
    active = models.BooleanField(default = True)

    #objects = models.Manager()
    filter_objects = managers.DescriptionManager()

    def __str__(self):
        return self.description

class GeneralInfo(models.Model):
    footer = models.OneToOneField(Footer, on_delete=models.CASCADE, related_name='general_footer')
    title = models.CharField(max_length=120, null = True)
    phone = models.CharField(max_length=14)
    ubication = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    active = models.BooleanField(default = True)

    #objects = models.Manager()
    filter_objects = managers.GeneralInfoManager()

    def __str__(self):
        return "Information "+self.footer.name

class SocialNetwork(models.Model):
    SOCIAL_NETWORK_ICON = [('mdi mdi-facebook','Facebook'), ('mdi mdi-twitter', 'Twitter'), ('mdi mdi-google-plus','Google+'),('mdi mdi-instagram', 'Instagram'), ('mdi mdi-youtube-play','Youtube')]

    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name='social_networks_footer')
    name = models.CharField(max_length=120)
    url = models.URLField()
    icon = models.CharField(max_length=40,choices=SOCIAL_NETWORK_ICON, default='mdi mdi-facebook')
    active = models.BooleanField(default = True)

    #objects = models.Manager()
    filter_objects = managers.SocialNetworkManager()

    def __str__(self):
        return self.name+" "+self.footer.name

class SubMenu(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name='submenu_footer')
    name = models.CharField(max_length=100)
    active = models.BooleanField(default = True)
    
    objects = models.Manager()
    filter_objects = managers.SubmenuManager()

    def __str__(self):
        return self.name+" "+self.footer.name

class ButtonSubmenu(models.Model):
    submenu = models.ForeignKey(SubMenu, on_delete= models.CASCADE, related_name='button_submenu')
    name = models.CharField(max_length=100)
    url = models.URLField(null=True)
    active = models.BooleanField(default = True)

    button_objects = managers.ButtonManager()


    def __str__(self):
        return self.name+"-Submenu "+self.submenu.name