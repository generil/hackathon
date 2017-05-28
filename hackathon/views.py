from django.shortcuts import render, redirect
from classroom.models import Record, Forum_Post
from registration.models import Person
# from registration.views import log_in


def home(request):
	if not request.user.is_authenticated:
		return redirect('log_in')

	records = Record.objects.filter(user = request.user)
	
	posts = []

	for record in records:
		classroom_forum_posts = Forum_Post.objects.filter(classroom = record.classroom)
		for post in classroom_forum_posts:
			posts.insert(0, post)

	person = Person.objects.get(id = request.user.id)
	context = {
		'records' : records, 
		'posts' : posts,
		'person' : person
	}
	return render(request, 'home.html', context=context)
