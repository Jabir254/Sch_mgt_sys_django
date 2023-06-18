from django.contrib import admin
from . models import std_mgt, Staff, LibraryRecord, Course_mgt, Attendance, Grade_mgt, Transcript, Timetable, Book, Finance, FeeCategory, Payment
# Register your models here.

@admin.register(std_mgt)
class std_mgtAdmin(admin.ModelAdmin):
    pass

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass

@admin.register(LibraryRecord)
class LibraryRecordAdmin(admin.ModelAdmin):
    pass

@admin.register(Course_mgt)
class Course_mgtAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Grade_mgt)
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



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass



