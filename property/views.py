from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import Property
from .forms import PropertyBookForm
from .filters import PropertyFilter
from django_filters.views import FilterView

class PropertyList(FilterView):
    model = Property
    paginate_by = 6
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'

class PropertyDetails(FormMixin, DetailView):
    model = Property
    form_class = PropertyBookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Property.objects.filter(category=self.get_object().category)[:2]
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['property'] = self.get_object() 
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()  
            form = self.get_form()
            if form.is_valid():
                myform = form.save(commit=False)
                myform.property = self.object
                myform.user = request.user
                myform.save()
                messages.success(request, "Booking created successfully!")
                return redirect('/property/')
            else:
                messages.error(request, "Please correct the errors in the form.")
                return self.form_invalid(form)
        except ObjectDoesNotExist:
            messages.error(request, "Property not found.")
            return redirect('/property/')