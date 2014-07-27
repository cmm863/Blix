from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from profiles.models import BlixUser
from profiles.forms import UserForm
from django.core.context_processors import csrf

# Create your views here.


def view_user_profile(request, username):
    return render_to_response('view_user_profile.html', {
        'user': get_object_or_404(BlixUser, username=username)
    })

def create_user(request):
    if request.POST:
        formf = UserForm(request.POST)

        formf.save()
        return HttpResponseRedirect('/')
    else:
        form = UserForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_user.html', args)