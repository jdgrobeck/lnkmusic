from django.shortcuts import render
from lnkmusic.models import Venue

def homepage(request):
    venues = Venue.objects.all()
    context = {'venues': venues}
    return render(request, 'index.html', context)

