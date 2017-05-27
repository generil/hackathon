# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# from hackathon import views
from models import User
from models import Person

def log_in(request):
    if request.user.is_authenticated:	
        return redirect('home')

    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            context['error_message'] = 'Invalid Username or Password'
            context['username'] = username

    return render(request, 'login.html', context=context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')

    context = {}
    data = {}

    if request.method == 'POST':
        data['username'] = request.POST.get('username')
        data['email'] = request.POST.get('email')
        data['password1'] = request.POST.get('password1')
        data['password2'] = request.POST.get('password2')

        dataCheck = user_integrityCheck(data)

        if dataCheck == True:
            created = User.objects.create_user(
            	username = data['username'], 
            	password = data['password1'],
            	email = data['email'])
            
            created.save()
            person = Person.objects.get(id = created.id)
            person.avatar = "default-user-avatar.png"
            # person.avatar.url = "/storage/default-user-avatar.png"
            person.save()
            
            user = authenticate(username = data['username'], password = data['password1'])
            login(request, user)

            print user
            return redirect('home')

        else:
            context = dataCheck[1]

    return render(request, 'register.html', context=context)


def user_integrityCheck(data):
    errors = {}

    if len(User.objects.filter(username = data.get('username'))) > 0:
        errors['username_error'] = "An account has this Username already. Pick another one."

        return False, errors

    if len(User.objects.filter(email = data.get('email'))) > 0:
        errors['email_error'] = "An account has this Email already. Pick another one."

        return False, errors

    if data.get('password1') != data.get('password2'):
        errors['password_error'] = "Passwords do not match"

    return True


def edit_profile_view(request):
  if not request.user.is_authenticated:
      return redirect('log_in')
  person = Person.objects.get(id = request.user.id)

  context = {
  	'person' : person,
  }
  return render(request, 'edit_profile.html', context)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('log_in')

    if request.method == 'POST':
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        user = request.user
        
        if new_first_name != '':
          user.first_name = new_first_name

        if new_last_name != '':
          user.last_name = new_last_name
        user.save()

        user_avatar = request.FILES.get('avatar')
        print user_avatar

        if user_avatar != None:
            fs = FileSystemStorage()
            user_avatar.name = 'user_' + str(request.user) + '_' + user_avatar.name
            filename = fs.save(user_avatar.name, user_avatar)

            person = Person.objects.get(id = request.user.id)
            person.avatar = filename
            person.save()

    return redirect('home')


def log_out(request):
  logout(request)

  return redirect('log_in')
