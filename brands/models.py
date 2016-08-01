from django.db import models

# Create your models here.

class Brand(models.Model):
	brand_name = models.CharField(max_length=255)
	link = models.CharField(max_length=255)
	

	def __unicode__(self):
		return self.brand_name
	
	
 	

