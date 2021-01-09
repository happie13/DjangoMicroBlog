from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
#model are databases in simpler terms
#to create a database,create  a class, and create its variables
User = settings.AUTH_USER_MODEL

class Blogmanager(models.Manager):
	def published_date(self):
		now = timezone.now
		return self.get_queryset().filter(pub_date__lte=now )


class model1(models.Model):
	title=models.CharField(max_length=120)
	image = models.ImageField(upload_to='image/',blank=True,null=True)
	info = models.TextField()
	slug = models.SlugField(unique = True)
	user = models.ForeignKey(User,default=1,null=True,on_delete = models.SET_NULL )
	pub_date = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title

	objects = Blogmanager()	

	class Meta:
		ordering = ["-pk","-pub_date","-updated","-timestamp"]

	# #conventional method to navigaate
	# def get_absolute_url(self):
	# 	return f'/app1/{self.name}'


	# def get_edit_url(self):
	# 	return f'/app1/{self.name}/edit'

	# def get_delete_url(self):
	# 	return f'/app1/{self.name}/delete'
	# 