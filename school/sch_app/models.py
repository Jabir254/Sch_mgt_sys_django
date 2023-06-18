from django.db import models
from django.utils import timezone

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField('Course', related_name='students')
    # Other fields and relationships


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField('Course', related_name='staff_members')
    # Other fields and relationships


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # Other fields and relationships


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='attendance_records')
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    # Other fields and relationships


class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    # Other fields and relationships


class Transcript(models.Model):
    transcript_id = models.AutoField(primary_key=True)
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    # Other fields and relationships


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='subjects')
    # Other fields and relationships


class ClassSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='class_schedules')
    time = models.TimeField()
    # Other fields and relationships


class Leave(models.Model):
    leave_id = models.AutoField(primary_key=True)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='leave_records')
    start_date = models.DateField()
    end_date = models.DateField()
    # Other fields and relationships


class LibraryRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='library_records')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='library_records')
    checkout_date = models.DateField()
    return_date = models.DateField()
    # Other fields and relationships


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    # Other fields and relationships


class Finance(models.Model):
    finance_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    fee_categories = models.ManyToManyField('FeeCategory', related_name='finances')
    # Other fields and relationships


class FeeCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    finance = models.ForeignKey('Finance', on_delete=models.CASCADE)
    # Other fields and relationships


class Fee(models.Model):
    fee_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='fee_records')
    fee_category = models.ForeignKey('FeeCategory', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields and relationships


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    fee_category = models.ForeignKey('FeeCategory', on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Other fields and relationships


class Timetable(models.Model):
    timetable_id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='timetables')
    day = models.CharField(max_length=255)
    time = models.TimeField()
    # Other fields and relationships


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    students = models.ManyToManyField('Student', related_name='teachers')
    parents = models.ManyToManyField('Parent', related_name='teachers')
    # Other fields and relationships


class Parent(models.Model):
    parent_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # Other fields and relationships

