from django.urls import path, include
from .views import (
	blogpost_list_view,
	blogpost_read_view,
)

app_name = 'blog'

urlpatterns = [
	path('', blogpost_list_view, name="home"), # ie blog:home blog/
	path('read/<post_title>/', blogpost_read_view, name="read"), # ie blog:read -> ex: blog/My First Post
	path('api/', include('blog.api.endpoints', namespace="blog_api")),
	
]
