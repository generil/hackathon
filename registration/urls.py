from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^sign-in/$', log_in, name='log_in'),
  url(r'^sign-up/$', sign_up, name='sign_up'),
  url(r'^log-out/$', log_out, name='log_out'),
  url(r'^edit-profile/$', edit_profile, name='edit_profile')
]