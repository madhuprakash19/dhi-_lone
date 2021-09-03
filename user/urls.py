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
    path('class/<int:class_id>/attendence_list/',views.attendence_list,name='attendence_list'),
    path('class/<int:attendence_id>/<int:class_id>/mark_attendence',views.mark_attendence,name='mark_attendence'),
    path('class/save_attendence/',views.save_attendence,name='save_attendence'),
]
