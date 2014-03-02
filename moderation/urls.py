from django.conf.urls import patterns, url
from moderation import views

urlpatterns = patterns('',
    url(r'^$', 'moderation.views.invite_member', name='moderators'),
    url(r'^resend/(?P<user_id>\d+)/$', 'moderation.views.resend_invitation', name='resend-invitation'),
    url(r'^revoke/(?P<user_id>\d+)/$', 'moderation.views.revoke_invitation', name='revoke-invitation'),
    url(r'^review-membership-applications$', 'moderation.views.review_applications', name='review-applications'),
    url(r'^review-abuse-reports$', 'moderation.views.review_abuse', name='review-abuse'),
    url(r'^logs$', 'moderation.views.view_logs', name='logs'),
)
