# Generated by Django 3.0.5 on 2020-11-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='M', max_length=6),
        ),
    ]
