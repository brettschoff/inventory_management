from django.db import models
from django.contrib.auth.models import User


class InventoryItem(models.Model):
	name = models.CharField(max_length=200)
	quantity = models.IntegerField()
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, blank=True, null=True)
	ISBN = models.CharField(max_length=200, default='Enter ISBN here')
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE) #if user deleted, all their invtoryitems are deleted

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=200)

	class Meta: 
		verbose_name_plural = 'authors'

	def __str__(self):
		return self.name
		
