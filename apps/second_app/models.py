from __future__ import unicode_literals
from django.db import models
from ..first_app.models import User
from django.db.models import F

class Secretmanager(models.Manager):
    def post(self, postdata):
        if postdata:
            self.create(secret=postdata['secret'],user_id=postdata['user_id'])

    def like(self, postdata):
        if postdata:
            Secret.objects.filter(user_likes=postdata['user_likes'])
            Secret.user_likes.add(request.session['id'])
            self.times_liked = F('times_liked') + 1
            return True

    def delete(self, postdata):
        if postdata:
            Secret.objects.filter(id=postdata['id']).delete()
            return True

    def sort(self):
        print Secret.objects.all()
        for x in self.all():
            print x
        return True

class Secret(models.Model):
    secret = models.CharField(max_length=500)
    user_likes = models.ManyToManyField(User, related_name='secrets_liked')
    times_liked = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, related_name='userid')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Secretmanager()
