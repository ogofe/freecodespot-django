from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def blogpost_list_view(request):
	template = 'blog-list.html'
	blogposts = BlogPost.objects.all().exclude(published=False)
	context = {
		'posts': blogposts,
	}
	return render(request, template, context)


def blogpost_read_view(request, post_title):
	template = 'blog-read.html'
	blogpost = BlogPost.objects.get(title=post_title)
	context = {
		'post': blogpost,
	}
	return render(request, template, context)




