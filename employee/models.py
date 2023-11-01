from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=64, default='')
    alias = models.CharField(max_length=64, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'employee'
        ordering = ['-id']


class EmployeeSalary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='employee_salary')
    salary = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'employee_salary'
        ordering = ['-id']