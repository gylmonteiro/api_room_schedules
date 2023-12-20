from django.db import models
from django.contrib.auth.models import User


# Create your models here.
JOB_TITLES_CHOCIES = (('P', 'Professor'),
                      ('C', 'Coordenador'),
                      ('D', 'Diretor'),
                      ('T', 'Técnico'))
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_full = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    job_title = models.CharField(choices= JOB_TITLES_CHOCIES, max_length=11, blank=True, null=True)

    def __str__(self):
        return self.name_full
