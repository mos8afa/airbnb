from django.shortcuts import render
from . import models
from django.views.generic import ListView

def about(request):
    what_we_do = models.WhatWeDo.objects.last()
    our_mission = models.OurMission.objects.last()
    our_goals = models.OurGoals.objects.last()
    image = models.AboutImage.objects.last()
    faqs = models.Faqs.objects.all()

    return render(request,'about/about.html',{
        'what_we_do':what_we_do,
        'our_mission':our_mission,
        'our_goals':our_goals,
        'image':image,
        'faqs':faqs
    })



