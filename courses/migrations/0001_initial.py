# Generated by Django 4.2.6 on 2023-10-08 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10, unique=True)),
                ('course_name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('year', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('course_status', models.CharField(choices=[('open', 'OPEN'), ('close', 'CLOSE')], default='open', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='courses.course')),
            ],
        ),
    ]