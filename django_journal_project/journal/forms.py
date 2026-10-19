from django import forms
from .models import Group, Student, Grade


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'group']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        # Включаем все поля, кроме даты (она будет добавляться автоматически)
        fields = ['student', 'subject', 'value']