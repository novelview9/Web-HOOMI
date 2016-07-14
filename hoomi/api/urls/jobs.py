from django.conf.urls import url, include

from api.views.jobs import *

urlpatterns = [
    url(r'^$', PhotoJobHistoryListAPIView.as_view(), name="photojob"),
    url(r'^(?P<hash_id>\w+)/$', ExperienceDetailListAPIView.as_view(), name="photojob"),
]
