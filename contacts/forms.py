from django import forms
from .models import Contact

#from snowpenguin.django.recaptcha2.fields import ReCaptchaField
#from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class ContactForm(forms.ModelForm):
    #captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta():
        model = Contact
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre...'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje...', 'rows':"4"}),
        }
