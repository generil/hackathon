from django.conf.urls import include, url
from . import views

app_name = 'classroom'

urlpatterns = [
	url(r'^add-classroom/$', views.add_classroom, name='add_classroom'),
	url(r'^(?P<pk>\d+)/forum/$', views.forum, name='forum'),
	url(r'^(?P<pk>\d+)/forum/post-forum/$', views.post_on_forum, name='post_on_forum'),
	url(r'^(?P<pk>\d+)/topic/$', views.topic, name='topic'),
	url(r'^(?P<pk>\d+)/forum/add-member$', views.add_member, name='add_member'),
	url(r'^(?P<pk>\d+)/topic/(?P<topic_id>\d+)/$', views.topic_details, name='topic_details'),
	url(r'^(?P<pk>\d+)/topic/(?P<topic_id>\d+)/add-post/$', views.post_on_topic, name='post_on_topic'),
	url(r'^(?P<pk>\d+)/topic/add-topic/$', views.add_topic, name='add_topic'),	
]
