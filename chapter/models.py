from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    ROLE_CHOICES = (
        ('owner', 'owner'),
        ('admin', 'admin'),
        ('organizer', 'organizer'),
        ('user', 'user'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


# Should person be related to a chapter ?
class Chapter(models.Model):
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)


class Venue(models.Model): 
    address = models.CharField(max_length=30)
    title = models.CharField(max_length=30)


class Event(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    img_url = models.URLField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)


class Rsvp(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    STATUSES = (
        ('Y', 'YES'),
        ('N', 'NO')
    )
    status = models.CharField(max_length=1, choices=STATUSES)


# After registering to an event, a person will get added to
# the mailing list. 
# Registraton will trigger an email as well as RSVP. 
# Reminder for upcoming events 

# Milestone 1 
# Create a user table 
