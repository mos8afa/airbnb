from django.urls import path
from . views import postList ,PostDetail

app_name = 'blog'

urlpatterns = [
    path('',postList.as_view(),name='post_list'),
    path('<slug:slug>',PostDetail.as_view(), name= "post_detail")
]
