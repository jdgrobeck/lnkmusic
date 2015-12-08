from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/venue/%s" % self.name_slug
     
   
class Genre(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/genre/%s" % self.name_slug

class Show(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    show_date = models.DateField()
    genre = models.ForeignKey(Genre)
    venue = models.ForeignKey(Venue)
    attendance = models.IntegerField()
    ticketprice = models.FloatField()
    grossrevenue = models.FloatField()
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/show/%s" % self.name_slug
    



