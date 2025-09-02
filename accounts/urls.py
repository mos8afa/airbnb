from django.urls import path
from .views import profile , profile_edit , signup ,my_list,my_reservations,add_list,add_category,add_place,activate


app_name = 'accounts'

urlpatterns = [
    path('signup',signup , name='signup'),
    path('profile/',profile,name='profile'),
    path('list/',my_list ,name='list'),
    path('reservations/',my_reservations ,name='reservations'),
    path('profile/edit', profile_edit , name='profile_edit') ,
    path('add_list/',add_list,name = 'add_list'),
    path('add_category/',add_category,name = 'add_category'),
    path('add_place/',add_place,name = 'add_place'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]


