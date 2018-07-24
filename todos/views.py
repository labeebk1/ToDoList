# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

# Todo App Views

def index(request):
	# Load Index page with a List of all ToDo Objects
	todos = Todo.objects.all()
	data = {'todos':todos}
	return render(request, 'index.html', data)

def details(request, id):
	# Retrieve selected To-Do and send object to Details Page
	todo = Todo.objects.get(id=id)
	data = {'todo':todo}
	return render(request, 'details.html', data)


def add(request):
	if(request.method == 'POST'):
		# Retrieve Title & Task from Form Submission
		title = request.POST['title']
		task = request.POST['task']

		# If To-Do Title & Task are empty, return to /todos
		if not title:
			return redirect('/todos')

		# Create new ToDo Object
		todo = Todo(title = title, task = task)

		# Save To-Do to list of To-Do Objects
		todo.save()

		return redirect('/todos')

	else:
		return render(request, 'add.html')


def delete(request, id):
	# Delete selected To-Do object
	todo = Todo.objects.get(id=id)
	todo.delete()
	return redirect('/todos')

def modify(request, id):
	if(request.method == 'POST'):
		# Retrieve Title & Task from Form Submission
		title = request.POST['title']
		task = request.POST['task']

		# If To-Do Title & Task are empty - return to /todos (modify nothing)
		if not title:
			return redirect('/todos')

		# Modify To-Do Object
		Todo.objects.filter(id=id).update(title=title)
		Todo.objects.filter(id=id).update(task=task)

		return redirect('/todos')

	else:
		# Retrieve selected To-Do and send object to Modify Page
		todo = Todo.objects.get(id=id)
		data = {'todo':todo}
		return render(request, 'modify.html', data)

