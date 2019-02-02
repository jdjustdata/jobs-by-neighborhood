"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView

from apps.site_admin.views import SignUpView, LoginView
from apps.home.views import redirect_language
admin.autodiscover()

urlpatterns = i18n_patterns(
    url(r'admin/main/', include('apps.site_admin.urls', namespace='site_admin')),
    # url(r'^admin/', include(admin.site.urls)), # this is the Django-provided admin module
    url(r'^admin/', RedirectView.as_view(pattern_name='login', permanent=False)),
    url(r'^accounts/login/', LoginView.as_view(template_name='site_admin/login.html'), name='login'),
    url(r'^accounts/logout/', LogoutView.as_view(template_name='site_admin/logout.html'), name='logout'),
    url(r'^accounts/register/$', SignUpView.as_view(template_name='site_admin/signup.html'), name='signup'),
    url(r'^business/', include('apps.business.urls', namespace='business')),
    url(r'^jobs/', include('apps.jobs.urls', namespace='jobs')),
    url(r'^', include('apps.home.urls', namespace="home"))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

urlpatterns.append(url(r'^', redirect_language))
