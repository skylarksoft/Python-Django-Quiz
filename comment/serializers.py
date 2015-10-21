from rest_framework import serializers

from entity.serializers import UserSerializer, PortfolioSerializer, InstrumentSerializer

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
	parent = serializers.SerializerMethodField('get_serialized_parent')

	SERIALIZERS = {
		'entity.user': UserSerializer,
		'entity.portfolio': PortfolioSerializer,
		'entity.instrument': InstrumentSerializer,
	}

	class Meta:
		model = Comment
		fields = ['id', 'comment', 'parent', ]
		read_only_fields = ['parent', ]

	def create(self, validated_data):
		obj = Comment(comment=validated_data['comment'], parent=validated_data['parent'])
		obj.comment = validated_data['comment']
		obj.parent = validated_data['parent']
		obj.save()
		return obj

	def get_serialized_parent(self, obj):
		content_type, pk = obj.content_type, obj.object_id
		if content_type and pk:
			model_class = content_type.model_class()
			try:
				instance = model_class.objects.get(pk=pk)
			except model_class.DoesNotExists:
				return None
			app_model = '{0}.{1}'.format(content_type.app_label,content_type.model)
			if app_model in self.SERIALIZERS.keys():
				serializer = self.SERIALIZERS[app_model]
			else:
				return None
			return serializer(instance=instance).data
		else:
			return None


class CommentListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
