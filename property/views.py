from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Property


class PropertyList(ListView):
    model = Property

class PropertyDetails(DetailView):
    model = Property
