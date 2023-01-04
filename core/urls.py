from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from core.account_management.views import dahboard
from core.account_management import views
from core.dashboard_site.views.home import index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('account/', include('core.account_management.urls', namespace='account')),
    path('admin_dashboard/', include('core.dashboard_site.urls', namespace='dashboard_site')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns = [
                      url(r'^media/(?P<path>.*)$', serve,
                          {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                  ] + staticfiles_urlpatterns() + urlpatterns
