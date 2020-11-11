from django.contrib import admin

# Register your models here.
from .models import Chapter, Event, Person, Rsvp, Venue

admin.site.site_header = "Chapter Admin"
admin.site.site_title = "Chapter Admin Area"
admin.site.index_title = "Welcome to the Chapter admin area"

admin.site.register(Chapter)
admin.site.register(Event)
admin.site.register(Person)
admin.site.register(Rsvp)
admin.site.register(Venue)
