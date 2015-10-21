from django.conf.urls import url
from .api import UserApi, PortfolioApi, InstrumentApi

urlpatterns = [
	url(r'^user/$', UserApi.as_view(), name='user_api'),
	url(r'^portfolio/$', PortfolioApi.as_view(), name='portfolio_api'),
	url(r'^instrument/$', InstrumentApi.as_view(), name='instrument_api'),
]

