from django.conf.urls import url
from django.contrib import admin

from scrap_group.views import GroupWall, user_id, UserDetails

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', GroupWall.as_view(), name='wall'),
    url(r'^user_id$', user_id, name='user_id'),
    url(r'^user_details$', UserDetails.as_view(), name='user_details'),
]
