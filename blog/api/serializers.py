from ..models import BlogPost
from rest_framework.serializers import ModelSerializer


class BlogPostSerializer(ModelSerializer):
	class Meta:
		model = BlogPost
		fields = ('id', 'title', 'author', 'content', 'display_image')



