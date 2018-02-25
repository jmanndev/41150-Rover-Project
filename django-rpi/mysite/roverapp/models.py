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