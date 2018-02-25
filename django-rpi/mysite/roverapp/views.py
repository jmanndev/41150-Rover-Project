# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import DataReceived

def index(request):
    data_list = DataReceived.objects.all()
    context = {
        'data_list' : data_list,
    }
    return render(request, 'roverapp/index.html', context)

# Create your views here.
