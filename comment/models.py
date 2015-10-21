from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
	comment = models.TextField()
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	parent = GenericForeignKey('content_type', 'object_id')
