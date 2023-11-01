# Generated by Django 4.1.2 on 2023-11-01 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesalary',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_salary', to='employee.employee'),
        ),
    ]
