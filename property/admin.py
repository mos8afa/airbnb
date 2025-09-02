from django.contrib import admin
from .models import Property , Place , PropertyBook , Category , PropertyImages 
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
    list_display = ['name','price_per_day']

admin.site.register(Property, SomeModelAdmin)
admin.site.register(Place)
admin.site.register(PropertyBook)
admin.site.register(Category)
admin.site.register(PropertyImages)


