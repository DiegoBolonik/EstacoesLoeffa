from django.db import models
from django import forms

CHOICES = (
    ('m', 'MANHÃ'),
    ('t', 'TARDE'),
    ('n', 'NOITE')
)


class Locais(models.Model):
    description = models.CharField(max_length=100, null=True)
    date = models.DateField(max_length=10, null=True)
    name = models.CharField(max_length=100)
    period = models.CharField(max_length=5, choices=CHOICES, null=True)

    def __str__(self):
        return self.description
