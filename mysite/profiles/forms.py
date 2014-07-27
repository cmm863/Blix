__author__ = 'connor'
from profiles.models import BlixUser
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = BlixUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]