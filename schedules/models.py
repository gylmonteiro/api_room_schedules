from django.db import models
from django.core.exceptions import ValidationError

from accounts.models import Account
# Create your models here.


class Time(models.Model):
    title = models.TextField(unique=True)
    justification = models.TextField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)


    def __str__(self):
        return f'{self.title} - {self.start_time} | {self.end_time}'


class Place(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(null=True, blank=True)
    max_occupation = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Schedule(models.Model):
    responsible = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='responsible', null=True)
    times = models.ManyToManyField(Time, related_name='times')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date = models.DateField()
    place = models.ForeignKey(Place, on_delete=models.PROTECT, related_name='place')

    def __str__(self):
        times_str = ', '.join(str(time) for time in self.times.all()) #if self.times.exists() else 'No times'
        return f'{self.responsible} - {self.date} | {times_str}'

