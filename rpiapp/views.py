from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from .forms import TabulationForm, SubjectForm, StudentForm
from .models import Subject


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
            temp = temp / sub_mark
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


class StudentCreateView(SuccessMessageMixin, CreateView):
    template_name = 'student_create.html'
    form_class = StudentForm

    def get_success_url(self):
        return reverse('student_create_view')

