from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('home/',views.HomePage.as_view(),name='home'),
    path('class/',views.ListClass.as_view(),name='all_class'),
    path('class/new/',views.CreatClassView.as_view(),name='new_class'),
    path('class/single/(?P<slug>[-\w]+)/',views.SingleClass.as_view(),name='single_class'),
    path('class/join/(?P<slug>[-\w]+)/',views.JoinClass.as_view(),name='join'),
    path('class/leave/(?P<slug>[-\w]+)/',views.LeaveClass.as_view(),name='leave'),

]
