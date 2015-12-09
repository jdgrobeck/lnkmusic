from django.shortcuts import render
from lnkmusic.models import Venue, Show

def homepage(request):
    venues = Venue.objects.all()
    context = {'venues': venues}
    return render(request, 'index.html', context)   
    
def venuedetail(request,venue_slug):
    venue = Venue.objects.get(name_slug=venue_slug)
    shows = Show.objects.filter(venue=venue).order_by('show_date')
    context = {'venue': venue, 'shows': shows}
    return render(request, 'venuedetail.html', context)   

def aboutdetail(request):
    context = {}
    return render(request, 'aboutdetail.html', context) 

    
