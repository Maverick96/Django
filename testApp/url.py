from django.conf.urls import include, url
from django.contrib import admin

#pattern
urlpatterns = [
    url(r'^pollApp/', include('pollApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]