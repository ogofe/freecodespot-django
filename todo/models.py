from django.db import models

# Create your models here.
class TodoListItem(models.Model):
	label = models.CharField(max_length=150)
	done = models.BooleanField(default=False) # set to false by default

	def __str__(self):
		return self.label


