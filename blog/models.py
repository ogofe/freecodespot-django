from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=250)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	published = models.BooleanField(default=False) # in draft by default
	content = models.TextField(blank=True, null=True)
	display_image = models.ImageField(upload_to='blog/images', blank=True, null=True)
	date_created = models.DateTimeField(auto_now=True)
	date_published = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		url = reverse('blog:read', kwargs={'post_title': self.title})
		return url



