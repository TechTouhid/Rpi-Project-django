from django.db import models


class Student(models.Model):
    SHIFT = (
        ('1', '1st'),
        ('2', '2nd'),
    )
    SEMESTER = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
    )

    SESSION = (
        ([tuple(str(str(str(int(i[0])) + '-' + str(int(i[0] + 1))) + ', ' + str(
            str(int(i[0])) + '-' + str(int(i[0] + 1)))).split(',')) for i in
          tuple(map(lambda *x: x, (tuple([i for i in range(2016, 2050)]))))])
    )

    DEPARTMENT = (
        ('computer', 'Computer'),
        ('civil', 'Civil'),
        ('electrical', 'Electrical'),
        ('electronics', 'Electronics'),
        ('mechanical', 'Mechanical'),
        ('power', 'Power'),
        ('electromedical', 'Electromedical'),
        ('mechatronics', 'Mechatronics'),
    )

    s_name = models.CharField(max_length=250, blank=True)
    s_roll = models.IntegerField(default=0, blank=True)
    s_reg = models.IntegerField(default=0, blank=True)
    s_sift = models.CharField(max_length=10, choices=SHIFT)
    s_semester = models.CharField(max_length=10, choices=SEMESTER)
    s_session = models.CharField(max_length=10, choices=SESSION)
    s_department = models.CharField(max_length=50, choices=DEPARTMENT)

    def __str__(self):
        return self.s_name


class Subject(models.Model):
    sub_name = models.CharField(max_length=120, default='')
    sub_code = models.IntegerField(default=0)
    sub_credit = models.IntegerField(default=0)
    full_mark = models.IntegerField(default=0)
    tc = models.IntegerField(default=0)
    tf = models.IntegerField(default=0)
    pc = models.IntegerField(default=0)
    pf = models.IntegerField(default=0)

    def __str__(self):
        return self.sub_name

class Tabulation(models.Model):

    # s_value = map(lambda *x:x, [str(i) for i in Subject.objects.all()])
    # # s_value = [tuple(str(i.sub_name).splitlines()) for i in Subject.objects.all()]
    # for i in s_value:
    #     print(i)
    #
    # SUBJECT = (
    #     (s_value, s_value),
    # )

    subject_code = models.CharField(max_length=120, null=True)
    tc = models.IntegerField()
    tf = models.IntegerField()
    pc = models.IntegerField()
    pf = models.IntegerField()
    gp = models.CharField(max_length=10)
    grade = models.CharField(max_length=10, null=True)
