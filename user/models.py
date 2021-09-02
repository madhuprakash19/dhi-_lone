from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

from django.contrib.auth.models import User


class CreateClass(models.Model):
    teacher = models.ForeignKey(User,related_name='handled_teacher',on_delete=models.CASCADE)
    sem = models.IntegerField()
    subject = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=20)
    students = models.ManyToManyField(User,through='ClassMember')
    slug = models.SlugField(allow_unicode = True,unique = True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.subject)
        super().save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse('user:all_class')

    def __str__(self):
        return self.subject

class ClassMember(models.Model):
    class_group = models.ForeignKey(CreateClass,related_name='student_member',on_delete = models.CASCADE)
    user = models.ForeignKey(User,related_name='user_class',on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('class_group','user')

class AttendenceList(models.Model):
    who = models.ForeignKey(CreateClass,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default = False )

    def __str__(self):
        return self.who.subject

class Attendence(models.Model):
    subject = models.ForeignKey(AttendenceList,on_delete=models.CASCADE)
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.subject.who.subject
