from django.contrib import admin
from .models import TodoListItem

# Register your models here.
# This will make the item available in the django admin
admin.site.register(TodoListItem)