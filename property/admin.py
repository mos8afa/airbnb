from django.contrib import admin
from .models import Property , Place , PropertyBook , Category , PropertyImages , PropertyReview 
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name','price_per_day','get_avg_rate']

admin.site.register(Property, SomeModelAdmin)
admin.site.register(Place)
admin.site.register(PropertyBook)
admin.site.register(Category)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)

