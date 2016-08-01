from django.db import models

from brands.models import Brand

# Create your models here.


class Product(models.Model):
	product_name = models.CharField(max_length=255)
	sku = models.PositiveIntegerField()
	link = models.CharField(max_length=255)
	brand = models.ForeignKey(Brand)
	 

	def __unicode__(self):
		return self.product_name
