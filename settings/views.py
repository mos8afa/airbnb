from django.shortcuts import render
from property import models
from . models import Settings
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import  Post
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.order_by('-created_at')[:4]
    places = models.Place.objects.all().annotate(property_count = Count('property_place'))
    categories = models.Category.objects.all()
    users_count = User.objects.all().count()
    hotels_count = models.Property.objects.all().count()
    places_count = models.Place.objects.all().count()
    settings =  Settings.objects.last()
    return render(request, 'settings/home.html', {
    'places': places,
    'categories': categories,
    'posts':posts,
    'users_count':users_count,
    'hotels_count':hotels_count,
    'places_count':places_count,
    'settings' : settings,
})


def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    property_list = models.Property.objects.filter(
        Q(name__icontains = name) &
        Q(place__name__icontains = place)
    )
    
    return render(request, 'settings/home_search.html',{'property_list': property_list})
    

def category_filter(request,category):
    category = models.Category.objects.get(name = category)
    property_list = models.Property.objects.filter(category = category)

    return render(request, 'settings/home_search.html',{'property_list': property_list})

def place_filter(request,place):
    place = models.Place.objects.get(slug=place)
    property_list = models.Property.objects.filter(place = place)

    return render(request,'settings/home_search.html',{'property_list': property_list})

