from django.db import models
from django.utils import timezone

# get the user table (one-to-many rel)
from django.contrib.auth.models import User

# Create your models here.
# each class is a Table in the database
# ORM : object relational mapper: access the DB in a OOP way
class Post(models.Model): 
	title = models.CharField(max_length=150)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#foreign key from table User
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title