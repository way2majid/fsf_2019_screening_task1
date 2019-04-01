# emApp, world's best Task Manager App

### Stay Connected ...

emApp is webapp written in Python using Django web-framework. It connects people in an organization and facilitates the formation of Teams and assignments of Tasks to those Teams

### Requirements

* Python 3.7 <br>
Other requirements are specified in **requirements.txt**<br>

### How to get started

* Download and install Python 3.7
* Open the Windows Command Prompt and create a virtual environment by using **mkvirtualenv [name]** command
* Enter into the virtual environment by typing **workon [name]** 
* Install the requirements: pip install -r requirements.txt
* Enter the **mysite** directory
* Make migrations : python manage.py makemigrations
* Migrate changes to the database : python manage.py migrate
* Run the server : python manage.py runserver
* Open http://127.0.0.1:8000/ in your browser, you'll see 

![](img/homepage_first.png)<br>

### How it works
<ul>
  <li> Allows a user to Sign-up </li>
  <li>Allows authenticated user to Log-in/ Sign-in</li>

![](img/Screenshot1.png)
![](img/Screenshot.png)

<li>Once the user has been authenticated, he/she will be taken to the Homepage. All the options are available on the Homepage</li>

![](img/homepage_user.png)<br>

<li> An authenticated user can do the following : 
<ul>
  <li> Create Tasks <li>

![](img/Screenshot2.png)

<li> Task will be registered in the database in the name of the currently logged-in user</li>

<li>Create Teams and assign members from among the authenticated users to that Team

![](img/Screenshot3.png)
<br>
<li> Team will be registered in the database in the name of the currently logged-in user</li>

<li> Assign Task to a Team ( Only those Tasks and Teams will be displayed that the currently logged-in user has created)</li><br>

![](img/Screenshot4.png)

<li> See what Tasks and Teams the current user has created and what Tasks he/she has assigned to other users</li>
  
  ![](img/your_creations.png)
  
 <li> Delete the Teams that the user has created. Only those Teams will be displayed in the dropdown menu that the currently logged-in user has created </li>

![](img/delete_team.png)

<li> Similarly we can delete Tasks. Only those Tasks will be displayed in the dropdown menu that the currently logged-in user has created</li>

<li> See those Teams of which the current user is a member, but not creator ( select <em>You are Team Member of</em> ...from the Homepage) </li>
  
  ![](img/team_member.png)
  
<li> See the Tasks that we have been assigned , by ourselves or by another user ( select <em>You are working on these Tasks</em> ... from the Homepage </li>

  ![](img/working_on_tasks.png)
  
 <ul>
  </li>
  
  <li> If a user forgets his/her password, then to access his account he/she will have to create a new password by selecting <em>Forgot your password</em> </li>
  
  ![](img/password1.png)
  
<li> The the user will have to enter his email address <li>
  
  ![](img/password2.png)
  
 <li> The following message will be displayed </li>
 
  ![](img/password3.png)
  
 <li> Actually no email has been sent. To activate this feature we will have to set up the SMTP server</li>
 

  
 

  
 
 




