# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from .models import Classroom
from .models import Topic
from .models import Topic_Post
from .models import Forum_Post
from .models import Topic_PostComment
from .models import Forum_PostComment

# Create your views here.

def add_classroom(request):
	if request.method == "POST":
		



def forum(request, pk):
	classroom = get_object_or_404(Classroom, pk=pk)
	posts = Forum_Post.objects.filter(clasroom=classroom)
	context = {
		'posts': posts
	}
	return render(request, 'classroom/forum.html', context=context)


def topic(request, pk):
	classroom = get_object_or_404(Classroom, pk=pk)
	topics = Topic.objects.filter(classroom=classroom)
	context = {
		'topics': topics,
		'classroom': classroom
	}
	return render(request, 'classroom/topics.html', context=context)


def add_topic(request, pk)
	classroom = get_object_or_404(Classroom, pk=pk)
	context = {
		'classroom': classroom
	}

	if request.method == "POST":
		name = request.POST.get('name')
		Topic.objects.create(classroom=classroom, name=name, creator=request.user)
		return redirect(reverse('topic', kwargs={'pk': classroom.pk))

	return render(request, 'classroom/add_topic.html', context=context)


def topic_details(request, pk, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	posts = Topic_Post.objects.filter(topic=topic)
	context = {
		'posts': posts
	}
	return render(request, 'classroom/topic_details.html', context=context)













