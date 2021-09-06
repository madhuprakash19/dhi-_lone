from django.contrib import admin
from user.models import CreateClass,ClassMember,AttendenceList,Attendence,MarksList,Marks
# Register your models here.

admin.site.register(CreateClass)
admin.site.register(ClassMember)
admin.site.register(AttendenceList)
admin.site.register(Attendence)
admin.site.register(MarksList)
admin.site.register(Marks)
