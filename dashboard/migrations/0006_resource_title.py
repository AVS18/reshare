# Generated by Django 3.1.2 on 2021-05-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210516_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]