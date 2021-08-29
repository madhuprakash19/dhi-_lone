from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from . import models
# Create your views here.

from . import forms

class SignUp(FormView):
    form_class = forms.UserCreateForm
    success_url='/account'
    template_name = 'accounts/signup.html'

    def form_valid(self,form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user_login = authenticate(username=username, password=password)
        p = models.UserProfileInfo(user=user_login)
        p.save()
        login(self.request, user_login)
        return HttpResponseRedirect(self.success_url)
