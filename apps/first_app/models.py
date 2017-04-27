from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User_manager(models.Manager):
    def register(self, postdata):
        error = []
        response_to_views = {}
        if postdata:
            if len(postdata['first_name']) < 2 and not re.search(r'^\w+$', postdata['first_name']):
                error.append('Please use two or more letters to write your first name.')
            elif len(postdata['last_name']) < 2 and not re.search(r'^\w+$', postdata['last_name']):
                error.append('Please use two or more letters to write your last name.')
            elif not EMAIL_REGEX.match(postdata['email']):
                error.append('Please use a correct email address.')
            elif len(postdata.get('password')) < 8 and postdata.get('password') != postdata.get('confirmpw'):
                error.append('Please correct your password fields. You must use at least 8 characters and both passwords must match.')
            elif User.objects.filter(email=postdata['email']):
                error.append('This email already exists, please choose another one.')
            else:
                password = bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt())
                self.create(email=postdata['email'],password=password,first_name=postdata['first_name'],last_name=postdata['last_name'])
        response_to_views['errors'] = error
        return response_to_views

    def signin(self, postdata):
        response_to_signin = {}
        idea = []
        user = User.objects.filter(email=postdata['email'])
        if postdata:
            if user:
                if bcrypt.hashpw(postdata['password'].encode(), user[0].password.encode()) == user[0].password.encode():
                    a = User.objects.filter(email=postdata['email'])
                    for z in a:
                        idea.append(z)
                    response_to_signin['id'] = idea
            return response_to_signin

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='password')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = User_manager()
