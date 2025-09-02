from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.html import format_html

class Property(models.Model):
    owner = models.ForeignKey(User,related_name='property_owner', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name",max_length=50)
    price_per_day = models.IntegerField(verbose_name='Price Per Day',default=0)
    description = models.TextField(verbose_name='Description', max_length=300)
    image = models.ImageField(verbose_name='Image',upload_to='property/')
    place = models.ForeignKey('Place',related_name='property_place',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',related_name='property_category',on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('property:property_details',kwargs={'slug':self.slug})
        
    def check_availability(self):
        reservations = self.book_property.all()
        today = timezone.now().date()

        for book in reservations:
            date_from = book.date_from.date()
            date_to = book.date_to.date()
            if today <= date_to and today >= date_from:
                return f'This room is booked until {date_to}'
            
            elif today < date_from:
                return f'This room is available until {date_from} or starting from the end of {date_to}'
            
        return 'Available'


class PropertyImages(models.Model):
    property = models.ForeignKey(Property,related_name='property_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return str(self.property)




class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')
    slug = models.SlugField(null=True,blank=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(Place, self).save(*args, **kwargs)



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

COUNT = (
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4), 
)

class PropertyBook(models.Model):
    user = models.ForeignKey(User,related_name='book_owner',on_delete=models.CASCADE)
    property = models.ForeignKey(Property,related_name='book_property',on_delete=models.CASCADE)
    date_from = models.DateTimeField(default=timezone.now)
    date_to = models.DateTimeField()
    guest = models.IntegerField(choices=COUNT)
    children = models.IntegerField(choices=COUNT)

    def __str__(self):
        return str(self.property)









