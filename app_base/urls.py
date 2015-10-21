from django.conf.urls import include, url

urlpatterns = [
	url(r'^', include('entity.urls', namespace='entity', app_name='entity')),
	url(r'^comment/', include('comment.urls', namespace='comment', app_name='comment')),
]

