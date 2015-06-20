from django.db import models

# Create your models here.

class user(models.Model):
	## Enter table columns for user field
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	email=models.CharField(max_length=20)
	password=models.CharField(max_length=8)

	def __str__(self):
		# shows the name of object in human readable format
		return self.firstname


class post(models.Model):
	## Relates to posts , associated with user
	user_post=models.ForeignKey(user)
	title=models.CharField(max_length=50)
	text=models.CharField(max_length=400)
	update_time=models.DateTimeField('date updated')		## inside '' denotes explanation to administrator 
	upvote=models.IntegerField(default=0)

	def __str__(self):
		return self.title
