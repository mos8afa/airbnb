from django.urls import path
from . views import home ,home_search,category_filter,place_filter

app_name ="settings"

urlpatterns = [
    path('', home, name='home'),
    path('home_search/', home_search, name ='home_search'),
    path('category/<slug:category>',category_filter,name='category_filter'),
    path('place/<slug:place>',place_filter,name="place_filter")

]
