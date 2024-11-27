from allauth.account.models import EmailAddress
from django.contrib import admin
from django.contrib.sites.models import Site
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('', include('core.urls')),

    # Third-party apps
    path('__debug__/', include('debug_toolbar.urls')),
]

admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
