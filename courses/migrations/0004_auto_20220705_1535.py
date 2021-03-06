# Generated by Django 3.2.12 on 2022-07-05 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.course')),
                ('sub_videos', models.FileField(upload_to='course')),
                ('sub_name', models.CharField(max_length=20)),
                ('sub_image_course', models.ImageField(upload_to='course')),
                ('sub_context', models.TextField(max_length=300)),
            ],
            bases=('courses.course',),
        ),
        migrations.RemoveField(
            model_name='course',
            name='videos',
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('video', 'video'), ('booklet', 'booklet')], default='booklet', max_length=10),
        ),
    ]
