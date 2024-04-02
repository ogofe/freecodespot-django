from django import forms
from .models import TodoListItem

class TodoForm(forms.ModelForm):
	label = forms.CharField()

	class Meta:
		model = TodoListItem
		fields = ['label', ]
