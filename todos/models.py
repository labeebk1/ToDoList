# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# To Do Class
class Todo(models.Model):
	# Title - Title of To-Do (200 Char Limit)
	title = models.CharField(max_length = 200)

	# Task - Task of To-Do (Text Field)
	task = models.TextField()

	# Created - Time Stamp of when To-Do was added
	created = models.DateTimeField(default=datetime.now, blank=True)
