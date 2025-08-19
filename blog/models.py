from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django .utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(verbose_name='Title',max_length=50)
    description = models.TextField(verbose_name='Content',max_length=1000)
    tags = TaggableManager()
    author = models.ForeignKey(User,related_name='posg_author',on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Post Image',upload_to='post/')
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category',related_name='post_category',on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    content = content = models.TextField(verbose_name='Comment',max_length=1000)
    created_at = created_at = models.DateTimeField(default=timezone.now)


    
