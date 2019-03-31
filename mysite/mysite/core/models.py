from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.
	


class Team(models.Model):
	team_name=models.CharField(max_length=100 )
	team_members=models.ManyToManyField(User)
	#task_assigned=models.OneToManyField(Task) # don't use on_delete with MntoMn Field

	class Meta:
		ordering=['team_name']

	def __str__(self):
		return self.team_name


class Task(models.Model):
	task_name=models.CharField(max_length=100)
	task_creator=models.ForeignKey(User, on_delete=models.CASCADE)
	team_assigned = models.ForeignKey(Team, on_delete=models.CASCADE)
	class Meta:
		ordering=['task_name']

	def __str__(self):
		return self.task_name



