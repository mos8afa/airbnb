from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView
from . models import Post , Category
from taggit.models import Tag
from django.db.models import Count
from django.db.models.query_utils import Q
from.froms import AddPost, AddCategory
from django.urls import reverse
from django.http import JsonResponse

class postList(ListView):
    model = Post
    template_name = 'blog\post.html'
    paginate_by = 8
    def get_queryset(self):
        name = self.request.GET.get('q','')
        object_list = Post.objects.filter(
            Q(title__icontains = name)|
            Q(description__icontains = name)
        )
        return object_list
    

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count = Count('post_category'))
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Post.objects.all()
        return context
    
class PostByCategory(ListView):
    template_name = 'blog\post.html'
    model = Post
    def get_queryset(self):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(category__name__icontains = slug)
        )
        return object_list
    

class PostByTag(ListView):
    template_name = 'blog\post.html'
    model = Post
    def get_queryset(self):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(tags__name__icontains=slug)
        )
        return object_list


def add_post(request):
    if request.method == 'POST':
        post_form = AddPost(request.POST,request.FILES)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect(reverse('blog:post_list'))
    else:
        post_form = AddPost()

    category_form = AddCategory()

    return render(request, "blog/add_post.html", {
        "post_form": post_form,
        "category_form": category_form,
    })

def add_category(request):
    if request.method == 'POST':
        category_form = AddCategory(request.POST)
        if category_form.is_valid():
            category_form.instance.author = request.user
            category = category_form.save()

            return JsonResponse({
                "id": category.id,
                "name": category.name
            })
        else:
            return JsonResponse({"errors": category_form.errors}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)


            

