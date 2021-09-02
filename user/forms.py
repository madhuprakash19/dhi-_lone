from . import models
from django import forms


class AttendenceForm(forms.ModelForm):
    class Meta:
        fields = ('date',)
        model = models.AttendenceList
