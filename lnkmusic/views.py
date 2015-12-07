from django.shortcuts import render
from lnkmusic.models import Venue

def homepage(request):
    venues = Venue.objects.all()
    context = {'venues': venues}
    return render(request, 'index.html', context)   
    
def venuedetail(request,venue_slug):
    venue = Venue.objects.get(name_slug=venue_slug)
    context = {'venue': venue}
    return render(request, 'venuedetail.html', context)   
    