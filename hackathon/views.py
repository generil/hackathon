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
=======
<<<<<<< HEAD
	return render(request, 'main.html', context=context)
=======
	
>>>>>>> b8852b2fa4db910d9c8e354485fd1cdf1539d338
	return render(request, 'home.html', context=context)

>>>>>>> 887ecbf070dd0a850b7d12fc34732c0a2fad0c9e
