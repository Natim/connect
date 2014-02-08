from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, ConnectPreference, UserLink
from skills.admin import UserSkillInline


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Profile'
    verbose_name_plural = 'Profile'


class UserLinkInline(admin.StackedInline):
    model = UserLink


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, UserSkillInline, UserLinkInline)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(ConnectPreference)
