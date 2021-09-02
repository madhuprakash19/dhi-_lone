from django.shortcuts import render
from django.views.generic import (TemplateView,DetailView,
                                CreateView,DetailView,
                                ListView,)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from accounts.models import UserProfileInfo
from . import models


class HomePage(LoginRequiredMixin,TemplateView):
    template_name = 'user/index.html'
    model = UserProfileInfo


class CreatClassView(LoginRequiredMixin,CreateView):
    fields=('sem','subject','subject_code')
    model = models.CreateClass
    context_object_name = 'class'
    template_name = 'user/class_form.html'
    success_url = '/user/class'

    def form_valid(self,form):

        classroom = form.save(commit=False)
        classroom.teacher = self.request.user
        classroom = classroom.save()
        return HttpResponseRedirect(self.success_url)

class SingleClass(LoginRequiredMixin,DetailView):
    model = models.CreateClass
    context_object_name = 'class'
    template_name = 'user/class_detail.html'

class ListClass(LoginRequiredMixin,ListView):
    model = models.CreateClass
    context_object_name = 'class'
    template_name = 'user/class_list.html'
