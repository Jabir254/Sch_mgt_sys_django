from django.db import models
# Create your models here.


class std_mgt(models.Model):

    # Fields for student records
    admission_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=10)

    # Fields for student registrations
    registration_date = models.DateField()
    registration_status = models.BooleanField(default=False)

    # Fields for attendance tracking
    attendance_date = models.DateField()
    is_present = models.BooleanField(default=False)

    # Fields for grading and performance monitoring
    subject = models.CharField(max_length=50)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    performance = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.admission_number})"


class Staff(models.Model):
    # Fields for staff details
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    teaching_assignments = models.ManyToManyField('Course_mgt',\
                                                  related_name='staff')

    # Fields for attendance tracking
    attendance_date = models.DateField()
    is_present = models.BooleanField(default=False)

    # Fields for leave management
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    leave_reason = models.TextField()
    is_approved = models.BooleanField(default=False)

    # Fields for salary administration
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    bank_account_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course_mgt(models.Model):
    """fields of course details"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True)
    management = models.ForeignKey('std_mgt', on_delete=models.SET_NULL,\
                                   null=True)

    def __str__(self):
        return self.name
