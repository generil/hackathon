# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Classroom(models.Model):
	name = models.CharField(max_length=100)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name + " - " + self.creator.username


class Record(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username + " - " + self.classroom.name
		

class Topic(models.Model):
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name + " - " + self.creator.username


class Topic_Post(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	content = models.CharField(max_length=5000)
	upvote = models.IntegerField(default=0)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.title + " - " + self.user.username


class Forum_Post(models.Model):
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	content = models.CharField(max_length=5000)
	upvote = models.IntegerField(default=0)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['date_created']

	def __str__(self):
		return self.title + " - " + self.user.username


class Topic_PostComment(models.Model):
	topic_post = models.ForeignKey(Topic_Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=500)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.user.username + " - " + self.content


class Forum_PostComment(models.Model):
	forum_post = models.ForeignKey(Forum_Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=500)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.user.username + " - " + self.content































