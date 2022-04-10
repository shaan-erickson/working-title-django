from django.db import models

class Venues(models.Model):
  venue_name = models.CharField(max_length=255)
  venue_manager = models.CharField(max_length=255)
