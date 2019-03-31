from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Team
from .forms import TaskForm, TeamForm


def home(request):
	count=User.objects.count()
	task=Task.objects.all().count()
	team=Team.objects.all().count()
	logged_in_user = request.user

	context={
			'count':count,
			'task':task,
			'team':team,
			'logged_in_user' : logged_in_user,
			}
	return render(request, 'home.html', context )
		
		

def signup(request):
	if request.method =='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'registration/primary_login.html' )
		
	else:
		form=UserCreationForm
	return render(request, 'registration/signup.html', {'form' : form})
	
@login_required	
def secret_page(request):
	return render(request, 'secret_page.html')

@login_required
def form(request):
	return render(request, 'form.html') # not being used

@login_required
def task_new(request):
	if request.method=="POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'success.html')

	else :
		print(request.user)
		form=TaskForm(initial={'task_creator': request.user})
	return render( request, 'task.html',{'form':form})


@login_required
def team_new(request):
	if request.method=="POST":
		form = TeamForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'success.html')

	else :
		form=TeamForm()
	return render( request, 'team.html',{'form':form})


def create_task(request):
	team_list = Team.objects.all()
	return render(request,'task.html',{'team_list' : team_list})
	

def create_task_process(request):
	if request.method == "POST":
		user = request.POST.get('user')
		user = get_object_or_404(User, username = user)
		team = request.POST.get('team')
		team = Team.objects.get(id = team)
		p = Task(	task_name = request.POST.get('task_name'),
					task_creator = user,
					team_assigned = team
			)
		p.save()
		return render(request,'success.html',{})
	return redirect('../home/')






