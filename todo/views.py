from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import TodoListItem




def home_view(request):
	form = TodoForm() # create an empty instance of the TodoForm

	# get all the todo list items and filter them based on the most recent,
	# excluding of course the one that have been done/completed
	todo_list = TodoListItem.objects.all().order_by('-id').exclude(done=True)
	
	# the relative path to your html file ie 'mysite/todo/templates/index.html'
	template = 'index.html'
	
	# check the url for a parameter to know if the user wants to mark an item as completed/done
	done = request.GET.get('todo_id', None) 
	
	if done: # if the parameter is not None eg done=1
		# get the item from the list with the id of done
		item = todo_list.get(id=done)
		item.done = True # set the todo item as done
		item.save() # save the changes

		# return to the home page 'todo' => view controller name, 'home' => route name
		return redirect('todo:home')


	if request.method == "POST": # when the todo form is submitted
		todo = TodoForm(request.POST) # create a new instance of the TodoForm with the form data
		
		# check if the values are correct/valid 
		# ie a string is sent when a string is expected and not an integer
		if todo.is_valid():
			todo.save() # create a todo item
			return redirect('todo:home') # return to the home page
		# raise Exception

	# Data to be passed to the template/html
	context = {
		'form': form, # the todo form instance
		'todo_list': todo_list # the list of all todos
	}

	return render(request, template, context)
