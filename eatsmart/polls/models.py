from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
#Models below

class Question(models.Model): #each Model is a Subclass of Model, Class name will be Table name
	question_text = models.CharField(max_length=200) #normal Text field
	pub_date = models.DateTimeField('date published') #Date field 
	
	def __str__(self):
		return self.question_text
		
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) #Defines a Relation to Question Many to One
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text