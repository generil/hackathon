from django.conf.urls import url

from registration import views

urlpatterns = [
	url(r'^login/$', views.log_in, name='log_in'),
	url(r'^signup/$', views.sign_up, name='sign_up'),
	url(r'^logout/$', views.log_out, name='log_out'),
	url(r'^edit-profile/$', views.edit_profile, name='edit_profile')
]