from django import forms
from .models import Subject, Student, Tabulation


class TabulationForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Tabulation
        fields = ['student_id', 's_semester', 's_roll', 'subject_code', 'tc', 'tf', 'pc', 'pf']

    def clean_tc(self, *args, **kwargs):
        tc = self.cleaned_data.get('tc')
        if tc > 50:
            raise forms.ValidationError("The integer must be les then or equal to 50")
        return tc

    def clean_tf(self, *args, **kwargs):
        tf = self.cleaned_data.get('tf')
        if tf > 50:
            raise forms.ValidationError("The integer must be les then or equal to 50")
        return tf

    def clean_pc(self, *args, **kwargs):
        pc = self.cleaned_data.get('pc')
        if pc > 50:
            raise forms.ValidationError("The integer must be les then or equal to 50")
        return pc

    def clean_pf(self, *args, **kwargs):
        pf = self.cleaned_data.get('pf')
        if pf > 50:
            raise forms.ValidationError("The integer must be les then or equal to 50")
        return pf

    def clean_subject_code(self, *args, **kwargs):
        subject_code = self.cleaned_data.get('subject_code')
        qs = Subject.objects.get(sub_code=subject_code)
        if qs:
            return subject_code
        else:
            raise forms.ValidationError("The subject not found in database")

    def clean_s_roll(self, *args, **kwargs):
        s_roll = self.cleaned_data.get('s_roll')
        qs = Student.objects.get(s_roll=s_roll)
        print(qs)
        if qs in Student.objects.all():
            print(qs)
            return s_roll
        else:
            raise forms.ValidationError("The roll not found in database")

class TabulationDetailsForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Tabulation
        exclude =['slug']






class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['sub_name', 'sub_code', 'sub_credit', 'full_mark', 'tc', 'tf', 'pc', 'pf']

    def clean_tc(self, *args, **kwargs):
        tc = self.cleaned_data.get('tc')
        if tc > 50:
            raise forms.ValidationError("The integer must be les then or equal to 50")
        return tc

    def clean_tf(self, *args, **kwargs):
        tf = self.cleaned_data.get('tf')
        if tf > 50:
            raise forms.ValidationError("The integer must be les then or equal to 50")
        return tf

    def clean_pc(self, *args, **kwargs):
        pc = self.cleaned_data.get('pc')
        if pc > 50:
            raise forms.ValidationError("The integer must be les then or equal to 50")
        return pc

    def clean_pf(self, *args, **kwargs):
        pf = self.cleaned_data.get('pf')
        if pf > 50:
            raise forms.ValidationError("The integer must be les then or equal to 50")
        return pf

    def clean_full_mark(self, *args, **kwargs):
        full_mark = self.cleaned_data.get('full_mark')
        if full_mark > 200:
            raise forms.ValidationError("The integer must be les then or equal to 200")
        return full_mark

    def clean_sub_credit(self, *args, **kwargs):
        sub_credit = self.cleaned_data.get('sub_credit')
        if sub_credit > 4:
            raise forms.ValidationError("The integer must be les then or equal to 4")
        return sub_credit





class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['s_name', 's_roll', 's_reg', 's_shift', 's_semester', 's_session', 's_department']
