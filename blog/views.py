from django.shortcuts import render
from django.views.generic import ListView , DetailView
from . models import Post , Category
from taggit.models import Tag

class postList(ListView):
    model = Post
    template_name = 'blog\post.html'
    paginate_by = 8

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Post.objects.all()
        return context


