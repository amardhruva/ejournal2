"""ejournal URL Configuration

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
from django.conf.urls import include
from django.contrib import admin
from django.urls.conf import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('author/', include('paperauthor.urls')),
    path('reviewer/', include('paperreviewer.urls')),
    path('api/', include('annotator.urls')),
    path('', include('baseportal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
