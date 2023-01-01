from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from core.account_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('core.account_management.urls', namespace='account')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns = [
                      url(r'^media/(?P<path>.*)$', serve,
                          {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                  ] + staticfiles_urlpatterns() + urlpatterns
