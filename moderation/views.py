from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

from .forms import InviteMemberForm


def create_username_from_email(email):
    """
    Cleans an email address to ensure it can be used as a
    username with django.contrib.auth.models.User
    """
    allowed_chars = '_@+.-'
    cleaned = ''

    for char in email:
        if char in allowed_chars or char.isalnum():
            cleaned += char

    if len(cleaned) > 30:
        cleaned = cleaned[:30]

    return cleaned


@login_required
def invite_member(request):
    """
    Allows a moderator to invite a new member to the system.
    """
    moderator = request.user

    if request.method == 'POST':
        form = InviteMemberForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            username = create_username_from_email(email)
            password = 'random'

            user = User.objects.create_user(username, email, password)

            user.is_active = False
            user.set_unusable_password()
            user.save()

            return redirect(reverse('moderators:moderators'))

    else:
        form = InviteMemberForm()

    context = {
        'form' : form,
    }

    return render(request, 'moderation/invite_member.html', context)


@login_required
def review_applications(request):
    context = ''
    return render(request, 'moderation/review_applications.html', context)


@login_required
def review_abuse(request):
    context = ''
    return render(request, 'moderation/review_abuse.html', context)


@login_required
def logs(request):
    context = ''
    return render(request, 'moderation/logs.html', context)