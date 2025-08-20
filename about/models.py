from django.db import models

class BaseAbout(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)


class WhatWeDo(BaseAbout):
    def __str__(self):
      return self.title

class OurMission(BaseAbout):
   def __str__(self):
        return self.title
    
class OurGoals(BaseAbout):
    def __str__(self):
      return self.title

class Faqs(BaseAbout):
    def __str__(self):
      return self.title
    
class AboutImage(models.Model):
   image = models.ImageField(upload_to='about/')
    

