from django.shortcuts import render

# Create your views here.

from django.views.generic import DeleteView,TemplateView,ListView,DetailView,CreateView,UpdateView
from app.models import *
from django.urls import reverse_lazy
class home(TemplateView):
    template_name='app/home.html'

class School_list(ListView):
    model=School
    template_name='app/School_list.html'
    context_object_name='schools'

class school_detail(DetailView):
    model=School
    context_object_name='scl'

class school_create(CreateView):
    model=School
    fields='__all__'

class schoolupdate(UpdateView):
    model=School
    fields='__all__'

class schooldelete(DeleteView):
    model=School
    context_object_name='school'
    success_url=reverse_lazy('School_list')
