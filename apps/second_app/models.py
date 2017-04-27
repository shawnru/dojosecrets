from __future__ import unicode_literals
from django.db import models
from ..first_app.models import User

class Secretmanager(models.Manager):
    def post(self, postdata):
        if postdata:
            user = User.objects.get(id=postdata['user_id'])
            self.create(secret=postdata['secret'],user_id=user)

    def like(self, postdata):
        if postdata:
            users = User.objects.get(id=postdata['userid'])
            secrets = Secret.objects.get(id=postdata['secid'])
            if not Secret.objects.filter(user_likes=users):
                secrets.user_likes.add(users)
                return True

    def delete(self, postdata):
        if postdata:
            Secret.objects.filter(id=postdata['id']).delete()
            return True

class Secret(models.Model):
    secret = models.CharField(max_length=500)
    user_likes = models.ManyToManyField(User, related_name='secrets_liked')
    user_id = models.ForeignKey(User, related_name='userid')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Secretmanager()
