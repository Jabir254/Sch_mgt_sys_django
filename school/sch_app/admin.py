from django.contrib import admin
from . models import Student, Staff, LibraryRecord, Course, Attendance, Grade,Transcript, Timetable, Book, Finance, FeeCategory,Teacher
# Register your models here.

@admin.register(Student)
class std_mgtAdmin(admin.ModelAdmin):
    pass

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass

@admin.register(LibraryRecord)
class LibraryRecordAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class Course_mgtAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Grade)
class Grade_mgtAdmin(admin.ModelAdmin):
    pass

@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    pass

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    pass

@admin.register(FeeCategory)
class FeeCategoryAdmin(admin.ModelAdmin):
    pass
