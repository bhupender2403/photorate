# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Album(models.model):
    displayname = models.CharField(max_length=255)
    

class AlbumFolder(models.model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    path = models.CharField(max_length=1024)
    
    
class Photo(models.model):
    
    displayname = models.CharField(max_length = 255)
    

class PhotoFile(models.model):
    album = models.ForeignKey(Photo,on_delete=models.CASCADE)
    parent = models.ForeignKey(Album,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    


    
class Rating(models.model):
    
    RATING_VALUE = (
    ('1','1 Star'),
    ('2','2 Star'),
    ('3','3 Star'),
    ('4','4 Star'),
    ('5','5 Star'),
    )
    
    album = models.ForeignKey(Photo,on_delete=models.CASCADE)
    value = models.CharField(max_length=1,choices = RATING_VALUE)

    