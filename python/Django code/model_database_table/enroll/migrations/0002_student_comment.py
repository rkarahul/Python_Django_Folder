# Generated by Django 4.1.3 on 2022-12-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='not avialble', max_length=40),
        ),
    ]
