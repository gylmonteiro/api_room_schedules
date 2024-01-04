from django.db import models


# Create your models here.

class Modality(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    CHOICES_PERIODS = (('M', 'MANHÃ'),
                       ('T', 'TARDE'),
                       ('N', 'NOITE'),
                       ('I', 'INTEGRAL'))

    level = models.IntegerField()
    period = models.CharField(max_length=1, blank=True, null=True, choices=CHOICES_PERIODS)
    modality = models.ForeignKey('Modality', related_name='series', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.level}º SÉRIE"


class Class(models.Model):
    name = models.CharField(max_length=155)
    students_number = models.IntegerField(default=0)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True, related_name='classes')

    def __str__(self):
        return self.name
