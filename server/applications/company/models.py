from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(
        max_length=250
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    link = models.CharField(
        max_length=250
    )
    foundation = models.IntegerField()
