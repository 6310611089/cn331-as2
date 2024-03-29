# Generated by Django 4.2.6 on 2023-10-09 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotaRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='seat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='CourseInfo',
        ),
        migrations.AddField(
            model_name='quotarequest',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quota_request', to='courses.course'),
        ),
        migrations.AddField(
            model_name='quotarequest',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
