from django.conf.urls import url
from django.contrib import admin

from scrap_group.views import GroupWall

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', GroupWall.as_view(), name='wall'),
]
