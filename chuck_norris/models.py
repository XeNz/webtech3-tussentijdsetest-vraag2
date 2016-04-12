from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=500)
	
	def __unicode__(self):
		return self.last_name

class Joke(models.Model):
	joke_text = models.CharField(max_length=300)
	joke_author = models.ForeignKey(Author)
	
	def __unicode__(self):
		return self.joke_text