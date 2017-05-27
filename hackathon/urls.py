from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from hackathon.views import home

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^admin/', admin.site.urls),
	url(r'^registration/', include('registration.urls')),
	url(r'^classroom/', include('classroom.urls')),
]
