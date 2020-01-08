from django.shortcuts import render
from django.views import generic
import json
from django.urls import reverse_lazy

from django.http import HttpResponse

from contacts.forms import ContactForm
from .models import Header, Service, Client, LogoClient
from footer.models import Footer, Description, GeneralInfo, SocialNetwork, SubMenu, ButtonSubmenu
from pages.models import Page

class HomePageView(generic.TemplateView):
    template_name = "base/content.html"    

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['header'] = Header.objects.filter(active=True)
        context['service'] = Service.objects.filter(active=True)
        context['client'] = Client.objects.filter(active=True)
        context['logoclient'] = LogoClient.objects.filter(active=True)

        context['descriptions'] = Description.filter_objects.all()
        context['generalinfos'] = GeneralInfo.filter_objects.all()
        context['socialnetworks'] = SocialNetwork.filter_objects.all()
        context['submenus'] = SubMenu.filter_objects.all()

        context['obras'] = Page.objects.filter(event_type='theater')
        context['events'] = Page.objects.filter(event_type='event')
        context['form'] = ContactForm()

        return context

class ContactCreateView(generic.FormView):
    #model = Course
    form_class = ContactForm
    template_name = "base/content.html"    
    success_url = reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs):        
        return super(ContactCreateView, self).dispatch(request, *args, **kwargs)
    

    def form_valid(self, form):            
        form.save()
        return super(ContactCreateView, self).form_valid(form)

    def form_invalid(self, form):
        content = {'errors': form.errors, 'success': False,}
        print (content)
        return HttpResponse(content=json.dumps(content), content_type='application/json; charset=utf-8')