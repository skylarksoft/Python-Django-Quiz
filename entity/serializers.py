from __future__ import absolute_import
from rest_framework import serializers

from .models import User, Portfolio, Instrument


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', )

	def to_representation(self, instance):
		rep = super(UserSerializer, self).to_representation(instance)
		rep['object_type'] = User.__name__.upper()
		return rep


class PortfolioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Portfolio

	def to_representation(self, instance):
		rep = super(PortfolioSerializer, self).to_representation(instance)
		rep['object_type'] = Portfolio.__name__.upper()
		return rep


class InstrumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instrument

	def to_representation(self, instance):
		rep = super(InstrumentSerializer, self).to_representation(instance)
		rep['object_type'] = Instrument.__name__.upper()
		return rep