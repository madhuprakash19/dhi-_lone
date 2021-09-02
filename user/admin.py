from django.contrib import admin
from user.models import CreateClass,ClassMember,AttendenceList,Attendence
# Register your models here.

admin.site.register(CreateClass)
admin.site.register(ClassMember)
admin.site.register(AttendenceList)
admin.site.register(Attendence)
