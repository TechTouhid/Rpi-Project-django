from django.test import TestCase

# Create your tests here.

# s = tuple(map(lambda *x: x, (tuple([i for i in range(2018, 2050)]))))
#
# for i in s:
#     print(tuple(str(str(str(int(i[0])) + '-' + str(int(i[0] + 1))) + ', ' + str(str(int(i[0])) + '-' + str(int(i[0] + 1)))).split(',')))
#


# x = ['Test subject', 'Test subject 2', 'Bangla', 'English']
#
# y = map(lambda *p: p, x)
# for i in y:
#
#     print(next(y))


# x = [('Test subject',), ('Test subject 2',), ('Bangla',), ('English',)]
s = (('Test subject',), ('Test subject 2',), ('Bangla',), ('English',))
#
# y = [x[i] for i in range(0,4)]
#
#
# def oo():
#     for i in range(0,4):
#         valu = x[i]
#         print(valu)
#
#
# print(oo())

# c = [101, 123, 100]
#
# x = tuple(s)
#
# for i in range(1, 1):
#     print(s)
#
# print(x)


def tabulations(request):
    template = 'tabulations.html'
    q_roll = request.GET.get('q_roll', None)
    q_semester = request.GET.get('q_semester', None)
    obj = Tabulation.objects.all()
    gpa = 0
    if q_roll and q_semester is not None:
        obj = obj.filter(s_roll=q_roll)
        obj = obj.filter(s_semester__iexact=q_semester)
        sub_count = obj
        s_credit = 0
        s_gp = 0

        for i in obj:
            sub_credit = Subject.objects.get(sub_code=i.subject_code)
            s_credit += sub_credit.sub_credit
            s_gp = (float(i.gp) * int(s_credit))

        gpa = s_gp / s_credit
        print(s_gp, s_credit, round(gpa))

        subject = Subject.objects.filter(sub_code__iexact=sub_credit.sub_code)
        student = Student.objects.get(s_roll=q_roll)
        print(student)
        context = {'obj': obj,
                   'gpa': gpa,
                   'subject': subject,
                   'student': student,
                   'sub_count': sub_count
                   }
        return render(request, template, context)
    return render(request, template, {})






def tabulations(request):
    template = 'tabulations.html'
    q_roll = request.GET.get('q_roll', None)
    q_semester = request.GET.get('q_semester', None)
    obj = Tabulation.objects.all()
    gpa = 0
    if q_roll and q_semester is not None:
        obj = obj.filter(s_roll=q_roll)
        obj = obj.filter(s_semester__iexact=q_semester)
        sub_count = obj
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

        for j in obj:
            increment += 1
            subject2 = Subject.objects.filter(sub_code__iexact=j.subject_code)
            if increment == 2:
                break
        increment = 0

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

        context = {'obj': obj,
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
                   'student': student,
                   'sub_count': sub_count
                   }
        return render(request, template, context)
    return render(request, template, {})