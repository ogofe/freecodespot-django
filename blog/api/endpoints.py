from django.urls import path, include
from .handlers import (
	blog_post_list_view,
	blog_post_read_view,
)

app_name = 'blog_api'

urlpatterns = [
	# ie blog_api:posts blog/api/posts
	path('posts/', blog_post_list_view, name="posts"),
	
	# ie blog_api:read -> ex: blog/api/posts/My First Post
	path('posts/<post_title>/', blog_post_read_view, name="read"),	
]
