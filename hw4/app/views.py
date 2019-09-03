from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib.auth.models import User
from app import models

def log_on(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
        except:
            return JsonResponse({'error': 'invalid parameters'})
        
        if models.User.objects.filter(username=username):
            return JsonResponse({'error': 'user exists'})
        else:
            user = models.User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'user': username})

def log_in(request):  
    if request.method == "POST":
        try:
            username = request.POST.get('username')
        except:
            return JsonResponse({'error': 'no such a user'})

        if username == '':
            return JsonResponse({'error': 'no such a user'})

        password = request.POST.get('password')

        if not models.User.objects.filter(username=username):
            return JsonResponse({'error': 'no such a user'})
        else:
            user = authenticate(username=username, password=password)
            if user and not request.user.is_authenticated:
                login(request, user)
                ret = JsonResponse({'user': username})
                request.session['username'] = username
                ret['Set-Cookie'] = "session_id=" + request.session['username']
                return ret
            else:
                if not request.user.is_authenticated:
                    return JsonResponse({'error': 'password is wrong'})
                else:
                    return JsonResponse({'error': 'has log in'})

def log_out(request):
    if request.method != "POST":
        return JsonResponse({'error': 'require POST'})
    if request.user.is_authenticated:
        username = request.session['username']
        logout(request)
        return JsonResponse({'user': username})
    else:
        return JsonResponse({'error': 'no valid session'})

def add_record(request):
    if request.user.is_authenticated:
        if request.method != "POST":
            return JsonResponse({'error': 'require POST'})
        else:
            try:
                time = request.POST.get('time')
                name = request.POST.get('name')
                content = request.POST.get('content')
                if name == '' or content == '' or not time.isdigit():
                    return JsonResponse({'error': 'invalid parameter'})
                record = models.Records()
                record.owner = request.user
                record.name = name
                record.time = time
                record.content = content
                record.save()
                return JsonResponse({'record_id': record.id})
            except:
                return JsonResponse({'error': 'invalid parameter'})
    else:
        return JsonResponse({'error': 'please login'})

def delete_record(request, id_num):
    if request.user.is_authenticated:
        if request.method != "POST":
            return JsonResponse({'error': 'require POST'})
        else:
            if not id_num.isdigit():
                return JsonResponse({'error': 'invalid parameter'})
            if not models.Records.objects.filter(id=id_num):
                return JsonResponse({'error': 'unknown record'})
            else:
                record = models.Records.objects.get(id=id_num)
                if record.owner != request.user:
                    return JsonResponse({'error': 'unknown record'})
                else:
                    record.delete()
                    return JsonResponse({'record_id': id_num})
    else:
        return JsonResponse({'error': 'please login'})

def update_record(request, id_num):
    if request.user.is_authenticated:
        if request.method != "POST":
            return JsonResponse({'error': 'require POST'})
        else:
            if not id_num.isdigit():
                return JsonResponse({'error': 'invalid parameter'})
            if not models.Records.objects.filter(id=id_num):
                return JsonResponse({'error': 'unknown record'})
            else:
                record = models.Records.objects.get(id=id_num)
                if record.owner != request.user:
                    return JsonResponse({'error': 'unknown record'})
                else:
                    try:
                        name = request.POST.get('name')
                        record.name = name
                    except:
                        pass
                    try:
                        time = request.POST.get('time')
                        record.time = time
                    except:
                        pass
                    try:
                        content = request.POST.get('content')
                        record.content = content
                    except:
                        pass

                    for key in request.POST:
                        if key != 'name' and key != 'time' and key != 'content':
                            return JsonResponse({'error': 'unknown record field'})
                    return JsonResponse({'record_id': id_num})
    else:
        return JsonResponse({'error': 'please login'})

def get_record(request, id_num):
    pass

def search_record():
    pass