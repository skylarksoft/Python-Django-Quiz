from django.db import models


class User(models.Model):
	name = models.CharField(max_length=256)


class Portfolio(models.Model):
	name = models.CharField(max_length=256)
	today_prc = models.FloatField()


class Instrument(models.Model):
	name = models.CharField(max_length=256)
	today_prc = models.FloatField()

