from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
	user = models.OneToOneField(User)
	avatar = models.FileField(blank = True)

	def __unicode__(self):
		return str(self.user)