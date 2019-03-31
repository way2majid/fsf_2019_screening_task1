from django import forms
from .models import Task, Team
from django.contrib.auth.models import User 

class TaskForm(forms.ModelForm):

	class Meta:
		model=Task
		fields=('task_name','task_creator','team_assigned')

class TeamForm(forms.ModelForm):

	class Meta:
		model=Team
		fields=('team_name','team_members',)



