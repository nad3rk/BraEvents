""" BRA Events URL Configuration """
# from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Impressum', views.imprint, name='imprint'),
    path('Datenschutz', views.dataprivacy, name='dataprivacy'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
