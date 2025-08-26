from django.urls import path
from .views import profile , profile_edit , signup ,my_list,my_reservations


app_name = 'accounts'

urlpatterns = [
    path('signup',signup , name='signup'),
    path('profile/',profile,name='profile'),
    path('list/',my_list ,name='list'),
    path('reservations/',my_reservations ,name='reservations'),
    path('profile/edit', profile_edit , name='profile_edit') ,
]
