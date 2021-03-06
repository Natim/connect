from django.conf.urls import patterns, include, url
from django.contrib.flatpages import urls as flatpages_urls
from django.utils.translation import ugettext_lazy as _

from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from accounts import urls as accounts_urls
from moderation import urls as moderation_urls
from discover import urls as discover_urls
from discover.views import dashboard


urlpatterns = patterns('',
    url(_(r'^admin/'), include(admin.site.urls)),
    url(r'^$', dashboard, name='dashboard'),
    url(_(r'^accounts/'), include(accounts_urls, namespace='accounts')),
    url(_(r'^moderation/'), include(moderation_urls, namespace='moderation')),
    url(_(r'^dashboard/'), include(discover_urls, namespace='discover')),
    url(_(r'^pages/'), include(flatpages_urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
