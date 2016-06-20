# # -*- coding: utf-8 -*-
"""About, Porfolio, Education and Experience Models."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class About(models.Model):
    """Contains the information of the about section of the portfolio."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    classes = models.CharField(max_length=100)

    def __str__(self):
        u"""WTF."""
        return self.title


@python_2_unicode_compatible
class Portfolio(models.Model):
    """Porfolio data, all except photos."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    site = models.CharField(max_length=500)
    repo = models.CharField(max_length=500)
    datafilter = models.CharField(max_length=100)
    application = models.CharField(max_length=255)
    display = models.CharField(max_length=30)

    def __str__(self):
        u"""WTF."""
        return self.title


@python_2_unicode_compatible
class Education(models.Model):
    """Information about my education."""

    institution = models.CharField(max_length=100)
    dates = models.CharField(max_length=100)
    degree = models.CharField(max_length=500)

    def __str__(self):
        u"""WTF."""
        return self.institution


@python_2_unicode_compatible
class Experience(models.Model):
    """Record of all my software experience."""

    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    dates = models.CharField(max_length=100)

    def __str__(self):
        u"""WTF."""
        return self.company
