from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts import models

# Create your views here.
class HomePage(LoginRequiredMixin,TemplateView):
    template_name = 'user/index.html'
    model = models.UserProfileInfo
