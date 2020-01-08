from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm
from django.views import generic



# Create your views here.
# class EventListView(generic.TemplateView):
#     template_name = "pages/page_list.html"
#     def get_context_data(self, **kwargs):
#         context = super(EventListView, self).get_context_data(**kwargs)
#         context['pages'] = Page.objects.filter(event_type='event')
#         return context

# class ObraListView(ListView):
#     template_name = "page_list.html"
#     model = Page
#     def get_context_data(self, **kwargs):
#         context = super(ObraListView, self).get_context_data(**kwargs)
#         context['pages'] = Page.objects.filter(event_type='theater')
#         return context


class PageDetailView(DetailView):
    model = Page

