from django.shortcuts import render

def home(request):
	dummy = 'DUMMY'
	context = {
	    'sample': dummy
	}
	return render(request, 'main.html', context=context)
