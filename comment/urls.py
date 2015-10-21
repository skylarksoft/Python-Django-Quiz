from django.conf.urls import url
from .api import CommentApi

urlpatterns = [
	url(r'^$', CommentApi.as_view(), name='comment_api'),
	url(r'^(?P<object_type>[-\w]+)/(?P<object_id>\d+)/$', CommentApi.as_view(), name='comment_api'),
	url(r'^(\d+)/(\d+)/$', CommentApi.as_view(), name='comment_api'),
]

