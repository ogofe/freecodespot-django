from django.contrib import admin
from .models import BlogPost
from datetime import datetime 

# Custom Admin InterFace for Blog Posts
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'post_author', 'published', 'date_created']
	search_fields = ['title', 'author']
	list_filter = ['author', 'published', 'date_created']
	list_display_links = ['title', 'post_author']
	actions = ['publish_all_posts', 'unpublish_all_posts']

	@admin.display(ordering="author__first_name")
	def post_author(self, obj):
		if obj.author.first_name:
			return f'{obj.author.first_name} {obj.author.last_name}'
		return obj.author.username

	def save_formset(self, request, form, formset, change):
		instances = formset.save(commit=False)

		if not change:
			for instance in instances:
				instance.author = request.user
				instance.save()
		formset.save_m2m()

	def publish_all_posts(self, request, queryset, **kwargs):
		queryset.update(published=True, date_published=datetime.now())
		return queryset

	def unpublish_all_posts(self, request, queryset, **kwargs):
		queryset.update(published=False, date_published=None)
		return queryset


# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)


admin.site.site_title = "My Site Admin"

admin.site.site_header = "My Site Admin"

admin.site.index_title = "Dashboard"




