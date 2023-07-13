""" BrighterVodka URL Configuration """
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # General pages
    path('', views.home, name='home'),

    
    path('Impressum', views.imprint, name='imprint'),
    path('Datenschutz', views.dataprivacy, name='dataprivacy'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )