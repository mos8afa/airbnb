from django.urls import path 
from .views import PropertyList, PropertyDetails
from .api_view import PropertyDetailApi , PropertyListApi

app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(), name = 'property_list' ),
    path('<slug:slug>',PropertyDetails.as_view(), name= "property_details"),
    path('api/',PropertyListApi.as_view(), name= 'property_list_api'),
    path('api/<int:pk>',PropertyDetailApi.as_view(), name= 'property_detail_api'),
]