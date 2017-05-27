from django.conf.urls import include, url
from . import views

app_name = 'classroom'

urlpatterns = [
<<<<<<< HEAD
	url(r'^add-classroom/$', view.add_classroom, name='add_classroom'),
	url(r'^(?P<pk>\d+)/forum/$', view.forum, name='forum'),
	url(r'^(?P<pk>\d+)/topic/$', view.topic, name='topic'),
	url(r'^(?P<pk>\d+)/topic/(?P<topic_id>\d+)/$', view.topic_details, name='topic_details'),
	url(r'^(?P<pk>\d+)/topic/(?P<topic_id>\d+)/add-post/$', view.add_topic_post, name='add_topic_post'),
	url(r'^(?P<pk>\d+)/topic/add-topic/$', view.add_topic, name='add_topic'),	
=======
	url(r'^add-classroom/$', views.add_classroom, name='add_classroom'),
	url(r'^(?P<pk>\d+)/forum/$', views.forum, name='forum'),
	url(r'^(?P<pk>\d+)/topic/$', views.topic, name='topic'),
	url(r'^(?P<pk>\d+)/topic/(?P<topic_id>\d+)/$', views.topic_details, name='topic_details'),
	url(r'^(?P<pk>\d+)/topic/add-topic/$', views.add_topic, name='add_topic'),	
>>>>>>> a96fccde3adf227fcbfd2a849ba7614cf9c8a120
]
