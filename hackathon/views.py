from django.shortcuts import render
from classroom.models import Record, Forum_Post
from registration.models import Person


def home(request):
	records = Record.objects.filter(user = request.user)
	
	posts = []

	for record in records:
		classroom_forum_posts = Forum_Post.objects.filter(classroom = record.classroom)
		for post in classroom_forum_posts:
			posts.append(post)

	person = Person.objects.get(id = request.user.id)
	context = {
		'records' : records, 
		'posts' : posts,
		'person' : person
	}
	return render(request, 'home.html', context=context)
