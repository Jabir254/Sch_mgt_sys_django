# Generated by Django 4.2.2 on 2023-06-14 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sch_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sch_app.std_mgt')),
                ('academic_year', models.CharField(max_length=10)),
                ('overall_gpa', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Grade_mgt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sch_app.course_mgt')),
                ('student_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sch_app.std_mgt')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_present', models.BooleanField(default=False)),
                ('staff_att', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sch_app.staff')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sch_app.std_mgt')),
            ],
        ),
    ]
