from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models
from django import forms

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()


class Upgradeform(forms.ModelForm):

    class Meta:
        fields = ('hod_status','teacher_status','student_status')
        model = models.UserProfileInfo
