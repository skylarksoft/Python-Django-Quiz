from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import User, Portfolio, Instrument
from .serializers import UserSerializer, PortfolioSerializer, InstrumentSerializer


class UserApi(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class PortfolioApi(generics.CreateAPIView):
	queryset = Portfolio.objects.all()
	serializer_class = PortfolioSerializer


class InstrumentApi(generics.CreateAPIView):
	queryset = Instrument.objects.all()
	serializer_class = InstrumentSerializer
