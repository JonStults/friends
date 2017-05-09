from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Users, Friends
import bcrypt
import re

def index(request):
    if 'user_id' not in request.session:
        request.session['user_id']= 0
    return render(request, 'friends/index.html')

def login(request):
    email = request.POST['email_login']
    enteredPW = request.POST['password_login']

    try:
        user = Users.objects.get(email = email)

    except:
        messages.warning(request, 'User does not exist!')
        return redirect('/')
    else:
        if bcrypt.hashpw(enteredPW.encode(), user.password.encode()) == user.password.encode():
            request.session['user_id'] = user.id
            return redirect('/friends')
        else:
            messages.warning(request, 'Password is incorrect!')
            return redirect('/')

def register(request):
    name = request.POST.get('name')
    alias = request.POST.get('alias')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_pw = request.POST.get('confirm_pw')
    date_of_birth = request.POST.get('date_of_birth')
    EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(name) < 1:
        messages.warning(request, 'Registration must not be blank')
        return redirect('/')
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.warning(request, 'Email is not a valid email')
        return redirect('/')
    if password != confirm_pw:
        messages.warning(request, 'Passwords do not match')
        return redirect('/')
    if len(password) < 8:
        messages.warning(request, 'Password needs to be at least 8 characters long')
        return redirect('/')
    else:
        password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
        result = Users.objects.create(name = name, alias = alias, email = email, password = password, date_of_birth = date_of_birth)
        request.session['user_id'] = result.id
        return redirect('/friends')


def friends(request):
    user = Users.objects.get(id = request.session['user_id'])
    friend = Friends.objects.filter(user_id = user.id)
    me = Friends.objects.filter(friend_id = user.id)
    others = Users.objects.exclude(id = user.id).exclude(friend__in = friend)
    context = {
            'user' : user,
            'others' : others,
            'friends' : friend
    }
    return render(request, 'friends/friends.html', context)


def profile(request, id):
    details = Users.objects.get(id = id)
    context = {
        'details' : details
    }
    return render(request, 'friends/profile.html', context)

def add_friend(request, id):
    friend = Friends.objects.create(user_id = Users.objects.get(id =request.session['user_id']), friend_id = Users.objects.get(id = id))
    if friend:
        print True
    else:
        print False
    return redirect('/friends')

def remove_friend(request,id):
    Friends.objects.get(id=id).delete()
    return redirect('/friends')

def logout(request):
    del request.session['user_id']
    return redirect('/')

# Create your views here.
