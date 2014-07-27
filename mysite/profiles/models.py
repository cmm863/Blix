from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlixUser(User):
    def __str__(self):
        return '%s' % self.username

    @models.permalink
    def get_absolute_url(self):
        return ('view_user_profile', None, { 'username': self.username })
