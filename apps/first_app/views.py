
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def register(request):
    if request.method == 'POST':
        if request.POST['register']:
            response_from_models = User.objects.register(request.POST)
            # try:
            if response_from_models['errors']:
                for error in response_from_models['errors']:
                    messages.error(request, error)
                    return redirect('logreg:logroot')
            else:
                messages.error(request, 'Please log-in with your new account.')
                return redirect('logreg:logroot')
            # except KeyError:
            #     return redirect('/success')

def login(request):
    if request.method == 'POST':
        try:
            response_from_signin = User.objects.signin(request.POST)
            if response_from_signin['id']:
                for a in response_from_signin['id']:
                    request.session['id'] = a.id
                return redirect('secrets:secroot')
            else:
                messages.error(request, 'No user in database')
                return redirect ('logreg:logroot')
        except KeyError:
            messages.error(request, 'No user in database')
            return redirect ('logreg:logroot')


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
