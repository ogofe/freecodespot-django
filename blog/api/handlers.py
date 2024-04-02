from .serializers import BlogPostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import BlogPost
from django.shortcuts import reverse


@api_view(["GET",])
def blog_post_list_view(request):
	posts = BlogPost.objects.all().exclude(published=False)
	data = {
		'posts': BlogPostSerializer(posts, many=True).data
	}
	return Response(data=data, status=200)


# Blog Post Reader View / Detail View for a Single Post
@api_view(["GET",])
def blog_post_read_view(request, post_title):
	post = BlogPost.objects.get(title=post_title)
	data = {
		'post': BlogPostSerializer(post).data
	}
	return Response(data=data, status=200)




