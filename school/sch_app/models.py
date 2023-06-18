from django.db import models
import random

class RandomIDField(models.AutoField):
    def get_random_id(self):
        # Generate a random ID
        return random.randint(1000, 9999)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            value = self.get_random_id()
        return value

# Create your models here.


class std_mgt(models.Model):

    # Fields for student records
    admission_number = RandomIDField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=10)

    # Fields for student registrations
    registration_date = models.DateField()
    registration_status = models.BooleanField(default=False)
 
    # Fields for grading and performance monitoring
    subject = models.ForeignKey('Course_mgt', on_delete=models.SET_NULL, null=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    performance = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.admission_number})"


class Staff(models.Model):
    # Fields for staff details
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    teaching_assignments = models.ManyToManyField('Course_mgt',
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

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student_name = models.ForeignKey('std_mgt', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    staff_att = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.student_name:
            return f"Student Attendance - {self.student_name.name} - {self.date}"
        elif self.staff_att:
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
    student = models.OneToOneField(std_mgt, on_delete=models.CASCADE,
                                   primary_key=True)
    academic_year = models.CharField(max_length=10)
    overall_gpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Transcript - {self.student.name} ({self.academic_year})"


class Timetable(models.Model):
    course_available = models.ForeignKey(Course_mgt, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    # Other fields related to timetable management

    def __str__(self):
        return f"Timetable - {self.course.name}\
            ({self.day_of_week}{self.start_time}-{self.end_time})"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    # Other fields related to book cataloging

    def __str__(self):
        return self.title


class LibraryRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(std_mgt, on_delete=models.CASCADE)
    issuance_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    # Other fields related to library management

    def __str__(self):
        return f"LibraryRecord - Book: {self.book.title},\
            Student: {self.student.name}"


class Finance(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Other fields related to finance management

    def __str__(self):
        return self.name


class FeeCategory(models.Model):
    name = models.CharField(max_length=100)
    finance = models.ForeignKey(Finance, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    # Other fields related to fee categories

    def __str__(self):
        return self.name


class Payment(models.Model):
    student = models.ForeignKey(std_mgt, on_delete=models.CASCADE)
    fee_category = models.ForeignKey(FeeCategory, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()

    # Other fields related to payment tracking

    def __str__(self):
        return f"Payment - {self.student.name} - {self.fee_category.name}"
