from django.db import models
# from django.utils.translation import getterxt_lazy as _

# Create your models here.

class Address(models.Model):
	street_name = models.CharField('street_name',max_length = 50)

	def __str__(self):
		return self.street_name