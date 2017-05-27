from django.shortcuts import render
from classroom.models import Record, Forum_Post


def home(request):
	records = Record.objects.filter(user = request.user)
	
	posts = []

	for record in records:
		classroom_forum_posts = Forum_Post.objects.filter(classroom = record.classroom)
		for post in classroom_forum_posts:
			posts.append(post)

	context = {
		'records' : records, 
		'posts' : posts,
	}
<<<<<<< HEAD

	return render(request, 'home.html', context=context)
=======
	return render(request, 'forum.html', context=context)
>>>>>>> 439e4b396741bf78b9d1a24dfe6393b28879aed1
