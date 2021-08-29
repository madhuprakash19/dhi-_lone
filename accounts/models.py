from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

	hod_status = models.BooleanField(default=False)
	teacher_status = models.BooleanField(default=False)
	student_status = models.BooleanField(default=True)

	def __str__(self):
		return self.user.username

	def hod(self):
		self.hod_status = True
		self.teacher_status = False
		self.student_status = False
		self.save()

	def teacher(self):
		self.hod_status = False
		self.teacher_status = True
		self.student_status = False
		self.save()
