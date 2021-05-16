# Generated by Django 3.1.2 on 2021-05-16 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_clamd.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_auto_20210516_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='resources', validators=[django_clamd.validators.validate_file_infection])),
                ('description', models.CharField(max_length=400)),
                ('branch', models.CharField(choices=[('ECE', 'ECE'), ('CSE', 'CSE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL'), ('OTHER', 'OTHER')], max_length=10)),
                ('year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]