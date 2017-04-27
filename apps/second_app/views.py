from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Secret
from ..first_app.models import User
from django.contrib import messages

def index(request):
    context = {
        'all_users': User.objects.all(),
        'all_secrets': Secret.objects.all(),
    }
    for x in Secret.objects.all():
        print x.user_id.id
    return render(request, 'second_app/index.html', context)

def like(request):
    if request.method == 'POST':
        Secret.objects.like(request.POST)
    return redirect('secrets:secroot')

def popular(request):
    context = {
        'all_users': User.objects.all(),
        'all_secrets': Secret.objects.all(),
        'curr_user': User.objects.get(id=request.session['id']),
    }
    x = User.objects.get(id=request.session['id'])
    print x.email
    return render(request, 'second_app/popular.html',context)

def addsecret(request):
    if request.method == 'POST':
        Secret.objects.post(request.POST)

    return redirect('secrets:secroot')

def delete(request):
    if request.method == 'POST':
        Secret.objects.delete(request.POST)
    return redirect('secrets:secroot')

def logout(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect('logreg:logroot')

# def session_test_1(request):
#     request.session['test'] = 'Session Vars Worked!'
#     return http.HttpResponseRedirect('done/?session=%s' % request.session.session_key)
#
# def session_test_2(request):
#     return http.HttpResponse('<br>'.join([
#         request.session.session_key,
#         request.GET.get('session'),
#         request.session.get('test', 'Session is Borked :(')
#          ]))
