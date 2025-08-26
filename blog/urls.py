from django.urls import path
from .  import views
from .api_view import post_list_api , post_detail_api ,post_search

app_name = 'blog'

urlpatterns = [
    path('',views.postList.as_view(),name='post_list'),
    path('api/posts/', post_list_api, name='post_list_api'),
    path('category/<slug:slug>',views.PostByCategory.as_view(), name= "post_by_category"),
    path('tags/<slug:slug>',views.PostByTag.as_view(), name= "post_by_tag"), 
    path('<slug:slug>',views.PostDetail.as_view(), name= "post_detail"), 
    path('api/posts', post_list_api, name='post_list_api'),
    path('api/posts/<int:id>',post_detail_api, name= "post_detail_api"), 
    path('api/posts/filter/<str:query>',post_search,name='post_search'),
]
