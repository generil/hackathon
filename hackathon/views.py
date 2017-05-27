from django.shortcuts import render

def home(request):
	dummy = 'DUMMY'
	context = {
	    'sample': dummy
	}
	return render(request, 'forum.html', context=context)
