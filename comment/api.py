from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

from entity.models import User, Portfolio, Instrument

from .models import Comment
from .serializers import CommentSerializer


class CommentApi(GenericAPIView, ListModelMixin):
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, object_type, object_id, *args, **kwargs):
		available_types = {
			'user': User,
			'portfolio': Portfolio,
			'instrument': Instrument,
		}
		if object_type not in available_types:
			raise PermissionDenied()

		_model = available_types[object_type]
		try:
			data = _model.objects.get(pk=object_id)
		except _model.DoesNotExists:
			raise PermissionDenied()

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(**dict(parent=data))

		return Response(serializer.data, status=status.HTTP_201_CREATED)

