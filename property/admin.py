from django.contrib import admin
from .models import Property , Place , PropertyBook , Category , PropertyImages , PropertyReview

admin.site.register(Property)
admin.site.register(Place)
admin.site.register(PropertyBook)
admin.site.register(Category)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)

