# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.urls import reverse

from .models import Classroom
from .models import Topic
from .models import Topic_Post
from .models import Forum_Post
from .models import Topic_PostComment
from .models import Forum_PostComment
from .models import Record
from registration.models import Person

from django.core.files.storage import FileSystemStorage

# Create your views here.

def forum(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	classroom = get_object_or_404(Classroom, pk=pk)
	posts = Forum_Post.objects.filter(classroom=classroom)
	records = Record.objects.filter(user=request.user)
	person = Person.objects.get(id = request.user.id)
	context = {
		'classroom': classroom,
		'posts': posts,
		'records': records,
		'person': person
	}
	return render(request, 'classroom/forum.html', context=context)


def topic(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	classroom = get_object_or_404(Classroom, pk=pk)
	topics = Topic.objects.filter(classroom=classroom)
	records = Record.objects.filter(user=request.user)
	person = Person.objects.get(id = request.user.id)
	context = {
		'topics': topics,
		'classroom': classroom,
		'records': records,
		'person': person
	}
	return render(request, 'classroom/topics.html', context=context)


def add_classroom(request):
	if not request.user.is_authenticated:
		return redirect('/')

	if request.method == "POST":
		name = request.POST.get('name')
		c = Classroom.objects.create(name=name, creator=request.user)
		Record.objects.create(user=request.user, classroom=c)
		c.save()
		return redirect(reverse('classroom:forum', kwargs={'pk': c.pk}))

	return redirect('/')


def add_topic(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	classroom = get_object_or_404(Classroom, pk=pk)
	topics = Topic.objects.filter(classroom=classroom)
	records = Record.objects.filter(user=request.user)
	person = Person.objects.get(id = request.user.id)
	context = {
		'classroom': classroom,
		'topics': topics,
		'records': records,
		'person': person
	}

	if request.method == 'POST':
		name = request.POST.get('name')
		Topic.objects.create(classroom=classroom, name=name, creator=request.user)
		return redirect(reverse('classroom:topic', kwargs={'pk': classroom.pk}))

	return render(request, 'classroom/add_topic.html', context=context)


def topic_details(request, pk, topic_id):
	if not request.user.is_authenticated:
		return redirect('/')

	classroom = get_object_or_404(Classroom, pk=pk)
	topic = get_object_or_404(Topic, pk=topic_id)
	posts = Topic_Post.objects.filter(topic=topic)
	records = Record.objects.filter(user=request.user)
	person = Person.objects.get(id = request.user.id)
	context = {
		'posts': posts,
		'topic': topic,
		'classroom': classroom,
		'records': records,
		'person': person
	}
	return render(request, 'classroom/topic_details.html', context=context)


def post_on_topic(request, pk, topic_id):
	if not request.user.is_authenticated:
		return redirect('/')

	classroom = get_object_or_404(Classroom, pk=pk)
	topic = get_object_or_404(Topic, pk=topic_id)

	if request.method == "POST":
		title = request.POST.get('title')
		content = request.POST.get('content')

		topic_post_file = request.FILES.get('file')

		if topic_post_file != None:
			fs = FileSystemStorage()
			topic_post_file.name = 'topic_post_' + str(topic) + '_' + topic_post_file.name
			filetype = get_file_type(topic_post_file.name)
			filename = fs.save(topic_post_file.name, topic_post_file)
			Topic_Post.objects.create(topic=topic, user=request.user, title=title, content=content, file=filename, filetype=filetype)

		else:
			Topic_Post.objects.create(topic=topic, user=request.user, title=title, content=content)

	return redirect(reverse('classroom:topic_details', kwargs={'pk': classroom.pk, 'topic_id': topic_id}))


def post_on_forum(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	redirect_url = request.GET.get('next')

	classroom = get_object_or_404(Classroom, pk=pk)

	if request.method == "POST":
		title = request.POST.get('title')
		content = request.POST.get('content')
			
		forum_post_file = request.FILES.get('file')

		if forum_post_file != None:
			fs = FileSystemStorage()

			filetype = get_file_type(forum_post_file.name)
			# forum_post_file.name = 'forum_post_' + str(topic) + '_' + forum_post_file.name
			filetype = get_file_type(forum_post_file.name)
			filename = fs.save(forum_post_file.name, forum_post_file)
			Forum_Post.objects.create(title=title, content=content, user=request.user, classroom=classroom, file=filename, filetype=filetype)

		else:
			Forum_Post.objects.create(title=title, content=content, user=request.user, classroom=classroom)

	return redirect(redirect_url)


def get_file_type(string):
	i = len(string) - 1
	filetype = ""
	while string[i] != '.':
		filetype += string[i]
		i -= 1
	return filetype[::-1]




	





	
