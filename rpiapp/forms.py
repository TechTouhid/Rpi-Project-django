from django import forms
from .models import Subject, Student, Tabulation

class TabulationForm(forms.ModelForm):

    class Meta:
        model = Tabulation
        fields = ['tc', 'tf', 'pc', 'pf']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['sub_name', 'sub_code', 'sub_credit', 'full_mark', 'tc', 'tf', 'pc', 'pf']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['s_name', 's_roll', 's_reg', 's_sift', 's_semester', 's_session', 's_department']