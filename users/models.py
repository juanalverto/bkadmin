from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)


	def __unicode__(self):
		return self.first_name