from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Person(models.Model):
	user = models.OneToOneField(User)
	avatar = models.FileField(blank = True)

	def __unicode__(self):
		return str(self.user)

def create_person(sender, instance, created, **kwargs):
	if created:
		profile, created = Person.objects.get_or_create(user=instance)

post_save.connect(create_person, sender = User)
