# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
    contextv = {
        'daysv':[1,2,3,4],
    }
    return render(request, 'index.html',  contextv)
