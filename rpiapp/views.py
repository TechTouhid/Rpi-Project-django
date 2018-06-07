from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import TabulationForm, SubjectForm, StudentForm


# Create your views here.
def tabulation(request):
    form = TabulationForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)

        def calculatu_marks():
            TC = obj.tc
            TF = obj.tf
            PC = obj.pc
            PF = obj.pf
            temp = (TC + TF + PC + PF) * 100
            print(temp)
            temp = temp / 200
            print(temp)
            if temp >= 80:
                gp = 4
                latter_grade = 'A+'
                return print(gp, latter_grade)

            elif temp >= 75:
                gp = 3.75
                latter_grade = 'A'
                return print(gp, latter_grade)

            elif temp >= 70:
                gp = 3.75
                latter_grade = 'A-'
                return print(gp, latter_grade)

            elif temp >= 65:
                gp = 3.25
                latter_grade = 'B+'
                return print(gp, latter_grade)

            elif temp >= 60:
                gp = 3.00
                latter_grade = 'B'
                return print(gp, latter_grade)

            elif temp >= 55:
                gp = 2.75
                latter_grade = 'B-'
                return print(gp, latter_grade)

            elif temp >= 50:
                gp = 2.50
                latter_grade = 'C+'
                return print(gp, latter_grade)

            elif temp >= 45:
                gp = 2.25
                latter_grade = 'C'
                return print(gp, latter_grade)

            elif temp >= 40:
                gp = 2.25
                latter_grade = 'D'
                return print(gp, latter_grade)
            else:
                gp = 0.00
                latter_grade = 'F'
                return print(gp, latter_grade)

        calculatu_marks()
    return render(request, 'tabulation.html', {'form': form})


class SubjectCreateView(SuccessMessageMixin, CreateView):
    template_name = 'subject_create.html'
    form_class = SubjectForm

    def get_success_url(self):
        return reverse('subject_create_view')


class StudentCreateView(SuccessMessageMixin, CreateView):
    template_name = 'student_create.html'
    form_class = StudentForm

    def get_success_url(self):
        return reverse('student_create_view')

# class Tabulation(CreateView):
#     template_name = 'tabulation.html'
#     form_class = TabulationForm
#     form = TabulationForm(request.POST)
