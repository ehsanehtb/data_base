# Generated by Django 3.1.6 on 2021-02-25 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blood',
            name='lab_employee_ID',
        ),
        migrations.RemoveField(
            model_name='blood',
            name='lab_tech_ID',
        ),
        migrations.DeleteModel(
            name='Lab_technician',
        ),
    ]