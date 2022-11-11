from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('allauth.urls')),
    # re_path('', include('social_django.urls', namespace='social')),
    path(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('cmsapp.urls')),
    path('', include('profile.urls')),
    path('', include('program.urls')),
    # keep this in the end otherwise it will rewrite index page
    path('', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

# the new django admin sidebar is bad UX in django CMS custom admin views.
admin.site.enable_nav_sidebar = False
