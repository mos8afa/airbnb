from django.urls import path
from .  import views

app_name = 'blog'

urlpatterns = [
    path('',views.postList.as_view(),name='post_list'),
    path('category/<slug:slug>',views.PostByCategory.as_view(), name= "post_by_category"),
    path('tags/<slug:slug>',views.PostByTag.as_view(), name= "post_by_tag"), 
    path('<slug:slug>',views.PostDetail.as_view(), name= "post_detail"), 
]
