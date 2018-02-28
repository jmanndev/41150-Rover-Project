# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import DataReceived
from .directions import forward, backward, left, right, up, down, idle

def index(request):
    data_list = DataReceived.objects.all()
    context = {
        'data_list' : data_list,
    }
    return render(request, 'roverapp/index.html', context)

# Create your views here.

def cforward(request):
    forward()
    return HttpResponseRedirect('/')


def cbackward(request):
    backward()
    return HttpResponseRedirect('/')


def cleft(request):
    left()
    return HttpResponseRedirect('/')


def cright(request):
    right()
    return HttpResponseRedirect('/')


def cidle(request):
    idle()
    return HttpResponseRedirect('/')


def cup(request):
    up()
    return HttpResponseRedirect('/')


def cdown(request):
    down()
    return HttpResponseRedirect('/')

