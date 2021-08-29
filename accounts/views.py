from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView,UpdateView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms

# from django.contrib.auth import get_user_model
# User = get_user_model()

class SignUp(FormView):
    form_class = forms.UserCreateForm
    success_url='/user/home/'
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

def Upgrade(request):
    current_user = request.user
    upgrade = get_object_or_404(models.UserProfileInfo,user=current_user)
    upgrade.teacher()
    return redirect('user:home')
