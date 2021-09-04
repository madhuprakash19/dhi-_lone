from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views.generic import (TemplateView,DetailView,
                                CreateView,DetailView,
                                ListView,RedirectView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import UserProfileInfo
from user.models import CreateClass,ClassMember,AttendenceList,Attendence
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AttendenceForm
from django.contrib.auth.models import User

class HomePage(LoginRequiredMixin,TemplateView):
    template_name = 'user/index.html'
    model = UserProfileInfo


class CreatClassView(LoginRequiredMixin,CreateView):
    fields=('sem','subject','subject_code')
    model = CreateClass
    context_object_name = 'class'
    template_name = 'user/class_form.html'
    success_url = '/user/class'

    def form_valid(self,form):
        classroom = form.save(commit=False)
        classroom.teacher = self.request.user
        classroom = classroom.save()
        return HttpResponseRedirect(self.success_url)

class SingleClass(LoginRequiredMixin,DetailView):
    model = CreateClass
    context_object_name = 'class'
    template_name = 'user/class_detail.html'

class ListClass(LoginRequiredMixin,ListView):
    model = CreateClass
    context_object_name = 'class'
    template_name = 'user/student_class_list.html'

@login_required()
def all_class(request):
    class_list = CreateClass.objects.filter( teacher=request.user )

    return render(request,'user/class_list.html',{'class_list':class_list,})




class JoinClass(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('user:single_class',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        classroom = get_object_or_404(CreateClass,slug=self.kwargs.get('slug'))

        try:
            ClassMember.objects.create(user=self.request.user,class_group=classroom)
        except IntegrityError:
            messages.warning(self.request,'Warning already a student of the class!')
        else:
            messages.success(self.request,'You are now a student of this class!')

        return super().get(request,*args,**kwargs)

class LeaveClass(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('user:single_class',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = ClassMember.objects.filter(
            user = self.request.user,
            class_group__slug = self.kwargs.get('slug')
            ).get()
        except ClassMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this class!')
        else:
            membership.delete()
            messages.success(self.request,'You hav left the class!')
        return super().get(request,*args,**kwargs)


@login_required()
def attendence_list(request,class_id):
    list_attendence = list(AttendenceList.objects.filter(who__id=class_id).order_by('-id'))

    if request.method == 'POST':
        attendence_form = AttendenceForm(data = request.POST)

        if attendence_form.is_valid():
            a = attendence_form.save(commit=False)
            a.who = get_object_or_404(CreateClass,id=class_id)
            a.save()
            attendence_id =a.id
            return HttpResponseRedirect(reverse('user:mark_attendence',args=[attendence_id,class_id]))
    else:
        attendence_form = AttendenceForm()
    return render(request,'user/attendence_list.html',{'attendence_form':attendence_form,'list_attendence':list_attendence,'class_id':class_id})

@login_required()
def mark_attendence(request,attendence_id,class_id):
    student_list = CreateClass.objects.filter( id = class_id )
    return render(request,'user/mark_attendence.html',
    {'attendence_id':attendence_id,'class_id':class_id,'student_list':student_list})


@login_required()
def edit_attendence(request,attendence_id,class_id):
    student_list = list(Attendence.objects.filter( subject__id = attendence_id ))
    return render(request,'user/edit_attendence.html',
    {'attendence_id':attendence_id,'class_id':class_id,'student_list':student_list})


@login_required()
def save_attendence(request):
    attendence_list = get_object_or_404(AttendenceList,id=request.POST['attendence_id'])
    class_id = request.POST['class_id']
    b = []
    student_class = get_object_or_404(CreateClass,id=class_id)
    for k in student_class.students.all():
        b.append(k.username)
    for i,j in request.POST.items():
        if i in b:
            status = j
            if status == 'present':
                status = True
            else:
                status = False
            if attendence_list.status == 1:
                try:
                    a = Attendence.objects.get(subject = attendence_list,student = get_object_or_404(User,username = i))
                    a.status = status
                    a.save()
                except Attendence.DoesNotExist:
                    a = Attendence(subject = attendence_list,student = get_object_or_404(User,username = i) , status = status)
                    a.save()
            else:
                a = Attendence(subject = attendence_list,student =get_object_or_404(User,username = i) , status = status)
                a.save()
                attendence_list.status = 1
                attendence_list.save()
    return HttpResponseRedirect(reverse('user:attendence_list',args=[class_id]))

@login_required()
def attendence_report(request,class_id):
    attendence_list = list(Attendence.objects.filter( subject__who__id = class_id ))
    list_attendence = list(AttendenceList.objects.filter(who__id=class_id))
    total_class = len(list_attendence)
    subject = get_object_or_404(CreateClass,id=class_id)
    report = {}
    for i in attendence_list:
        if i.student.username in report:
            if i.status:
                report[i.student.username] = report[i.student.username] + 1
        else:
            if i.status:
                report[i.student.username] = 1
            else:
                report[i.student.username] = 0

    return render(request,'user/attendence_report.html',{'report':report,'subject':subject,'total_class':total_class})
