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
    return render(request, 'second_app/index.html', context)

def like(request):
    if request.method == 'POST':
        return redirect('secrets:secroot')
    else:
        return redirect('secrets:secroot')

def popular(request):
    Secret.objects.sort()
    context = {
        'all_users': User.objects.all(),
        'all_secrets': Secret.objects.all(),
    }
    return render(request, 'second_app/popular.html')


def delete(request):
    if request.method == 'POST':
        if Secret.objects.delete(request.POST):
            return redirect('secrets:secroot')
        else:
            return redirect('secrets:secroot')

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
