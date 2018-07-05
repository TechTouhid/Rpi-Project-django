from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.encoding import smart_text


class Student(models.Model):
    SHIFT = (
        ('1', '1st'),
        ('2', '2nd'),
    )
    SEMESTER = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
        ('5th', '5th'),
        ('6th', '6th'),
        ('7th', '7th'),
        ('8th', '8th'),
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

    s_name = models.CharField(max_length=250, blank=True, verbose_name='Name')
    s_roll = models.IntegerField(default=0, blank=True, verbose_name='Roll')
    s_reg = models.IntegerField(default=0, blank=True, verbose_name='Registration')
    s_sift = models.CharField(max_length=10, choices=SHIFT, verbose_name='Shift')
    s_semester = models.CharField(max_length=10, choices=SEMESTER, verbose_name='Semester')
    s_session = models.CharField(max_length=10, choices=SESSION, verbose_name='Session')
    s_department = models.CharField(max_length=50, choices=DEPARTMENT, verbose_name='Department')
    slug = models.SlugField(unique=True, null=True)

    # def __str__(self):
    #     return self.s_roll

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.s_name:
                self.slug = slugify(self.s_name)
        super(Student, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('student_details_view', kwargs={"slug": self.slug})

    def __str__(self):  # Using this rename the model name
        return smart_text(str('Name: ' + self.s_name + ' ' + 'Roll: ' + str(self.s_roll)))


class Subject(models.Model):
    sub_name = models.CharField(max_length=120, default='', verbose_name='Name')
    sub_code = models.IntegerField(unique=True, default=0, verbose_name='Code')
    sub_credit = models.IntegerField(default=0, verbose_name='Credit')
    full_mark = models.IntegerField(default=0, verbose_name='Full Mark')
    tc = models.IntegerField(default=0, verbose_name='TC')
    tf = models.IntegerField(default=0, verbose_name='TF')
    pc = models.IntegerField(default=0, verbose_name='PC')
    pf = models.IntegerField(default=0, verbose_name='PF')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.sub_name

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.sub_name:
                self.slug = slugify(self.sub_name)
        super(Subject, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('subject_details_view', kwargs={"slug": self.slug})

    def __str__(self):  # Using this rename the model name
        return smart_text(self.sub_name)


class Tabulation(models.Model):
    # s_value = map(lambda *x:x, [str(i) for i in Subject.objects.all()])
    # # s_value = [tuple(str(i.sub_name).splitlines()) for i in Subject.objects.all()]
    # for i in s_value:
    #     print(i)
    #
    # SUBJECT = (
    #     (s_value, s_value),
    # )

    SEMESTER = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
        ('5th', '5th'),
        ('6th', '6th'),
        ('7th', '7th'),
        ('8th', '8th'),
    )

    student_id = models.ForeignKey(Student, null=True, on_delete=models.CASCADE, verbose_name='Student Id')
    s_roll = models.IntegerField(default=0, blank=True, verbose_name='Student Roll')
    s_semester = models.CharField(max_length=10, null=True, choices=SEMESTER, verbose_name='Student Semester')
    subject_code = models.CharField(max_length=120, null=True, verbose_name='Subject Code')
    tc = models.IntegerField(default=0, verbose_name='TC')
    tf = models.IntegerField(default=0, verbose_name='TF')
    pc = models.IntegerField(default=0, verbose_name='PC')
    pf = models.IntegerField(default=0, verbose_name='PF')
    gp = models.CharField(max_length=10, verbose_name='GP')
    grade = models.CharField(max_length=10, null=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.s_roll and self.s_semester and self.subject_code:
                self.slug = slugify(str(self.s_roll) + '-' + self.s_semester + '-' + str(self.subject_code))
        super(Tabulation, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tabulation_details_view', kwargs={"slug": self.slug})


    def __str__(self):  # Using this rename the model name
        return smart_text(str(self.student_id) + ' semester : ' + str(self.s_semester))
