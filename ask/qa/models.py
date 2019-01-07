from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
       title = models.CharField(max_length=255)
       text = models.TextField()
       added_at = models.DateTimeField(blank=True)
       rating = 
       author = 
       likes = 
def __unicode__(self):
return self.title
def get_absolute_url(self):
return '/post/%d/' % self.pk
class Meta:
db_table = 'blogposts'
ordering = ['-creation_date']



class Answer(models.Model):
       text = models.TextField()
       added_at = models.DateTimeField(blank=True)
       question = 
       author = 
def __unicode__(self):
return self.title
def get_absolute_url(self):
return '/post/%d/' % self.pk
class Meta:
db_table = 'blogposts'
ordering = ['-creation_date']
