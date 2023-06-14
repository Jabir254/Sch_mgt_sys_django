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

class Attendance(models.Model):
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    student = models.ForeignKey(std_mgt, on_delete=models.CASCADE, null=True, blank=True)
    staff_att = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.student:
            return f"Student Attendance - {self.student.name} - {self.date}"
        elif self.Staff:
            return f"Staff Attendance - {self.staff_att.name} - {self.date}"
        else:
            return f"Attendance - {self.date}"


class Grade_mgt(models.Model):
    """Grade of each student"""
    student_grade = models.ForeignKey(std_mgt, on_delete=models.CASCADE)
    course = models.ForeignKey(Course_mgt, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    # Other fields related to grading

    def __str__(self):
        return f"Grade - {self.student_grade.name} ({self.course.name})"


class Transcript(models.Model):
    student = models.OneToOneField(std_mgt, on_delete=models.CASCADE, primary_key=True)
    academic_year = models.CharField(max_length=10)
    overall_gpa = models.DecimalField(max_digits=4, decimal_places=2)


    def __str__(self):
        return f"Transcript - {self.student.name} ({self.academic_year})"
