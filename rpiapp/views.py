from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import ModelFormMixin, UpdateView

from .forms import TabulationForm, SubjectForm, StudentForm, TabulationDetailsForm
from .models import Subject, Student, Tabulation


class MultipleObjectMixin(object):
    def get_object(self, queryset=None, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            try:
                obj = self.model.objects.get(slug=slug)
                return obj
            except self.model.MultipleObjectsReturned:
                obj = self.get_queryset().first()
            except:
                obj = None
            return obj
        return Http404

def home(request):
    return render(request, 'home.html', {})

# Create your views here.
def tabulation(request):
    form = TabulationForm(request.POST or None)
    if form.is_valid():
        obj = form.save()

        def calculatu_marks():
            sub_mark = Subject.objects.get(sub_code=obj.subject_code)
            sub_mark = sub_mark.full_mark
            tc = obj.tc
            tf = obj.tf
            pc = obj.pc
            pf = obj.pf
            temp = (tc + tf + pc + pf) * 100
            print(temp)
            temp = temp / sub_mark
            print(temp)
            if temp >= 80:
                obj.gp = 4
                obj.grade = 'A+'
                return obj.gp, obj.grade

            elif temp >= 75:
                obj.gp = 3.75
                obj.grade = 'A'
                return obj.gp, obj.grade

            elif temp >= 70:
                obj.gp = 3.75
                obj.grade = 'A-'
                return obj.gp, obj.grade

            elif temp >= 65:
                obj.gp = 3.25
                obj.grade = 'B+'
                return obj.gp, obj.grade

            elif temp >= 60:
                obj.gp = 3.00
                obj.grade = 'B'
                return obj.gp, obj.grade

            elif temp >= 55:
                obj.gp = 2.75
                obj.grade = 'B-'
                return obj.gp, obj.grade

            elif temp >= 50:
                obj.gp = 2.50
                obj.grade = 'C+'
                return obj.gp, obj.grade

            elif temp >= 45:
                obj.gp = 2.25
                obj.grade = 'C'
                return obj.gp, obj.grade

            elif temp >= 40:
                obj.gp = 2.25
                obj.grade = 'D'
                return obj.gp, obj.grade
            else:
                obj.gp = 0.00
                obj.grade = 'F'
                return obj.gp, obj.grade

        calculatu_marks()
        print(calculatu_marks())
        obj = form.save()
    return render(request, 'tabulation.html', {'form': form})


class SubjectCreateView(SuccessMessageMixin, CreateView):
    template_name = 'subject_create.html'
    form_class = SubjectForm

    def get_success_url(self):
        return reverse('subject_create_view')


class SubjectListView(ListView):
    model = Subject
    template_name = 'subject_list_view.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(SubjectListView, self).get_queryset(*args, **kwargs)
        return qs


class SubjectDetailView(SuccessMessageMixin, ModelFormMixin, MultipleObjectMixin, DetailView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_details_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SubjectDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                self.form_valid(form)

    def get_success_url(self):
        return reverse('subject_details_view')


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_update_view.html'


class StudentCreateView(SuccessMessageMixin, CreateView):
    template_name = 'student_create.html'
    form_class = StudentForm

    def get_success_url(self):
        return reverse('student_create_view')


class StudentListView(ListView):
    model = Student
    template_name = 'student_list_view.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentListView, self).get_queryset(*args, **kwargs)
        return qs


class StudentDetailView(SuccessMessageMixin, ModelFormMixin, MultipleObjectMixin, DetailView):
    model = Student
    form_class = StudentForm
    template_name = 'student_details_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(StudentDetailView, self).get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                self.form_valid(form)

    def get_success_url(self):
        return reverse('subject_details_view')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_update_view.html'


def tabulations(request):
    template = 'tabulations.html'
    q_roll = request.GET.get('q_roll', None)
    q_semester = request.GET.get('q_semester', None)
    obj = Tabulation.objects.all()
    gpa = 0
    if q_roll and q_semester is not None:
        obj = obj.filter(s_roll=q_roll)
        obj = obj.filter(s_semester__iexact=q_semester)
        print(obj.count())
        object = obj
        s_credit = 0
        s_gp = 0

        for i in obj:
            sub_credit = Subject.objects.get(sub_code=i.subject_code)
            s_credit += sub_credit.sub_credit
            s_gp = (float(i.gp) * int(s_credit))

        gpa = s_gp / s_credit
        print(s_gp, s_credit, round(gpa))

        student = Student.objects.get(s_roll=q_roll)
        print(student)
        subject = ''
        subject1 = None
        subject2 = None
        subject3 = None
        subject4 = None
        subject5 = None
        subject6 = None
        subject7 = None
        subject8 = None
        subject9 = None
        subject10 = None
        increment = 0


        for i in obj:
            increment += 1
            subject1 = Subject.objects.filter(sub_code__iexact=i.subject_code)
            if increment == 1:
                break
        increment = 0
        print(subject1)
        for j in obj:
            increment += 1
            subject2 = Subject.objects.filter(sub_code__iexact=j.subject_code)
            if increment == 2:
                break
        increment = 0
        print(subject2)
        for i in obj:
            increment += 1
            subject3 = Subject.objects.filter(sub_code__iexact=i.subject_code)
            if increment == 3:
                break
        increment = 0

        for i in obj:
            increment += 1
            subject4 = Subject.objects.filter(sub_code__iexact=i.subject_code)
            if increment == 4:
                break
        increment = 0

        for i in obj:
            increment += 1
            subject5 = Subject.objects.filter(sub_code__iexact=i.subject_code)
            if increment == 5:
                break
        increment = 0

        for i in obj:
            increment += 1
            subject6 = Subject.objects.filter(sub_code__iexact=i.subject_code)
            if increment == 6:
                break
        increment = 0

        for i in obj:
            increment += 1
            subject7 = Subject.objects.filter(sub_code__iexact=i.subject_code)
            if increment == 7:
                break
        increment = 0

        for i in obj:
            increment += 1
            subject8 = Subject.objects.filter(sub_code__iexact=i.subject_code)
            if increment == 8:
                break
        increment = 0

        for i in obj:
            increment += 1
            subject9 = Subject.objects.filter(sub_code__iexact=i.subject_code)
            if increment == 9:
                break
        increment = 0

        for i in obj:
            increment += 1
            subject10 = Subject.objects.filter(sub_code__iexact=i.subject_code)
            if increment == 10:
                break
        print(subject1.last())
        print(subject2.last())

        context = {'obj': object,
                   'gpa': gpa,
                   'subject1': subject1.last(),
                   'subject2': subject2.last(),
                   'subject3': subject3.last(),
                   'subject4': subject4.last(),
                   'subject5': subject5.last(),
                   'subject6': subject6.last(),
                   'subject7': subject7.last(),
                   'subject8': subject8.last(),
                   'subject9': subject9.last(),
                   'subject10': subject10.last(),
                   'student': student
                   }
        return render(request, template, context)
    return render(request, template, {})


class TabulationDetailView(SuccessMessageMixin, ModelFormMixin, MultipleObjectMixin, DetailView):
    model = Tabulation
    form_class = TabulationDetailsForm
    template_name = 'tabulation_details_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TabulationDetailView, self).get_context_data(*args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                self.form_valid(form)

    def get_success_url(self):
        return reverse('tabulation_details_view')
