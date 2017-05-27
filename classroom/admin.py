# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Classroom
from .models import Topic
from .models import Topic_Post
from .models import Forum_Post
from .models import Topic_PostComment
from .models import Forum_PostComment

admin.site.register(Classroom)
admin.site.register(Topic)
admin.site.register(Topic_Post)
admin.site.register(Forum_Post)
admin.site.register(Topic_PostComment)
admin.site.register(Forum_PostComment)