from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Venues

def index(request):
  venues = Venues.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'venues': venues,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['venue_name']
    y = request.POST['venue_manager']
    venue = Venues(venue_name=x, venue_manager=y)
    venue.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    x = Venues.objects.get(id=id)
    x.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    myvenue = Venues.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'myvenue': myvenue,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    name = request.POST['venue_name']
    manager = request.POST['venue_manager']
    venue = Venues.objects.get(id=id)
    venue.venue_name = name
    venue.venue_manager = manager
    venue.save()
    return HttpResponseRedirect(reverse('index'))