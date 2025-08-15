from django.db import models

#class BaseAbout(models.Model):
 #   title = models.CharField(max_length=100)
  #  content = models.TextField(max_length=1000)


#class WhatWeDo(BaseAbout):
 #   def __str__(self):
  #      return self.title

#class OurMission(BaseAbout):
 #   def __str__(self):
  #      return self.title
    
#class OurGoals(BaseAbout):
 #   def __str__(self):
  #      return self.title

#class Faqs(BaseAbout):
 #   def __str__(self):
  #      return self.title

#class Image(models.Model):
 #   image = models.ImageField(upload_to='about/')

class About (models.Model):
    what_we_do = models.TextField(max_length=2000)   
    our_mission = models.TextField(max_length=2000) 
    our_goals = models.TextField(max_length=2000) 
    image = models.ImageField(upload_to='about/')
    #faqs = models.ForeignKey('FAQS',related_name='faqs',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    

    
class FAQS(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

