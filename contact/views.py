from django.shortcuts import render
from settings.models import Settings


def contact(request):
    settings = Settings.objects.last()  
    
    return render(request, 'contact/contact.html', {
        'name':settings.site_name,
        'address': settings.address,
        'phone': settings.phone,
        'email': settings.email,
        'fb_link': settings.fb_link,
        'instagram_link': settings.instagram_link,
    })
