from django.conf.urls import url
from django.contrib import admin

from scrap_group.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^code$', Code.as_view(), name='code'),
    url(r'^step1$', SendMessagesOne.as_view(), name='send-messages-one'),
    url(r'^step2$', SendMessagesTwo.as_view(), name='send-messages-two'),
    url(r'^step3$', SendMessagesThree.as_view(), name='send-messages-three'),

    url(r'^group_wall$', GroupWall.as_view(), name='wall'),
    url(r'^user_id$', user_id, name='user_id'),
    url(r'^user_details$', UserDetails.as_view(), name='user_details'),
]
