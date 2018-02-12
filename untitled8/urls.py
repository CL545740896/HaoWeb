"""untitled8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
handler404 = 'Face.views.page_not_found'
handler500 = 'Face.views.page_not_found'
from django.conf import settings
urlpatterns = [
    url(r'^HaoyidaiAdmin/', 'Face.views.admin',name='admin'),
    url(r'^love$', 'Face.views.upload_file', name='upload'),
    url(r'^index$', 'Face.views.index', name='index'),
    url(r'^result$', 'Face.views.result', name='result'),
    url(r'^message$', 'Face.views.GetMessage', name='message'),
    url(r'^register$', 'Face.views.register', name='register'),
    url(r'^login$', 'Face.views.login', name='login'),
    url(r'^user$', 'Face.views.user', name='user'),
    url(r'^page$', 'Face.views.page', name='page'),
    url(r'^danmu$', 'Face.views.danmu', name='danmu'),
    url(r'^insert$', 'Face.views.insert', name='insert'),
    url(r'^logout$', 'Face.views.logout', name='logout'),
    url(r'^sendMsg$', 'Face.views.SendMsg', name='sendMsg'),
    url(r'^adminLogin$', 'Face.views.adminLogin', name='adminLogin'),
]
# if settings.DEBUG is False:
#     urlpatterns += ('',
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,
#         }),
#    )
# else:
urlpatterns += staticfiles_urlpatterns()