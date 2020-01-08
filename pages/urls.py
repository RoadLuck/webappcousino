from django.urls import path
from .views import PageDetailView

urlpatterns = [
    # path('event/', EventListView.as_view(), name='event'),
    # path('obra/', ObraListView.as_view(), name='obra'),
    path('page/<int:pk>/', PageDetailView.as_view(), name='page'),

]
    
