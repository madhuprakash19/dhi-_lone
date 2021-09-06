from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('home/',views.HomePage.as_view(),name='home'),
    path('class/',views.all_class,name='all_class'),
    path('class/new/',views.CreatClassView.as_view(),name='new_class'),
    path('class/single/(?P<slug>[-\w]+)/',views.SingleClass.as_view(),name='single_class'),
    path('class/join/(?P<slug>[-\w]+)/',views.JoinClass.as_view(),name='join'),
    path('class/leave/(?P<slug>[-\w]+)/',views.LeaveClass.as_view(),name='leave'),
    path('class/<int:class_id>/attendence_list/',views.attendence_list,name='attendence_list'),
    path('class/<int:attendence_id>/<int:class_id>/mark_attendence/',views.mark_attendence,name='mark_attendence'),
    path('class/save_attendence/',views.save_attendence,name='save_attendence'),
    path('class/<int:attendence_id>/<int:class_id>/edit_attendence/',views.edit_attendence,name='edit_attendence'),
    path('class/all/',views.ListClass.as_view(),name='student_class'),
    path('class/<int:class_id>/attendence_report/',views.attendence_report,name='attendence_report'),
    path('class/<int:class_id>/marks_list/',views.marks_list,name='marks_list'),
    path('class/<int:marks_list_id>/<int:class_id>/enter_marks/',views.enter_marks,name='enter_marks'),
    path('class/<int:marks_list_id>/<int:class_id>/edit_marks/',views.edit_marks,name='edit_marks'),
    path('class/save_marks/',views.save_marks,name='save_marks'),
    path('marks_report/',views.marks_report,name='marks_report'),

]
