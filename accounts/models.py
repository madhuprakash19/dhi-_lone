from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)

	hod_status = models.BooleanField(default=False)
	teacher_status = models.BooleanField(default=False)
	student_status = models.BooleanField(default=True)

	def __str__(self):
		return self.user.username
