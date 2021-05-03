from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	name = models.CharField(max_length=100)
	noofchallengessolved=models.IntegerField()
	expertiselevel=models.IntegerField()
	datastructure=models.IntegerField()
	algo=models.IntegerField()
	cpp=models.IntegerField()
	java=models.IntegerField()
	python=models.IntegerField()
	vote=models.IntegerField()


class ip(models.Model):
	ipaddress=models.CharField(max_length=100,unique=True)

		
