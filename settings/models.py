from django.db import models

class Settings(models.Model):
    site_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="settings/")
    address = models.TextField(max_length=500)
    email = models. EmailField(max_length=300)
    phone = models.CharField(max_length=13)
    description = models.TextField(max_length=1500)
    fb_link = models.URLField(max_length=200)
    x_link = models.URLField(max_length=200)
    instagram_link = models.URLField(max_length=200)

    def __str__(self):
        return self.site_name