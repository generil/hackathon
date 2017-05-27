# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . models import Person
from django.db.models.signals import post_save

admin.site.register(Person)
