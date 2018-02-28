# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DataReceived(models.Model):
  sendTime = models.CharField(max_length=200)
  heading = models.CharField(max_length=200)
  roll = models.CharField(max_length=200)
  pitch = models.CharField(max_length=200)
  tempC = models.CharField(max_length=200)
  leftState = models.CharField(max_length=200)
  rightState = models.CharField(max_length=200)
  propellorState = models.CharField(max_length=200)
  distance = models.CharField(max_length=200)
  def __str__(self):
    return '%s | %sC | Dist:%s | Heading:%s' % (self.sendTime, self.tempC, self.distance, self.heading)
