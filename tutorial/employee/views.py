    from django.shortcuts import render
    from .models import Employee, EmployeeSalary
    from django.http import HttpResponse 
    from rest_framework import status
    # Create your views here.
    import json
     
    def index(request):
        if request.method == "GET":
            employee_list = list(Employee.objects.all().values())
            res = {
                "data": employee_list
            }
            return HttpResponse(json.dumps(res, default=str, indent=4), status=status.HTTP_200_OK)
     
        if request.method == "POST":
            data=json.loads(request.body)
            name=data['name']
            alias=data['alias']
            salary=data["salary"]
     
            employee = Employee.objects.create(
                name=name,
                alias=alias
            )
            
            salary = EmployeeSalary.objects.create(
                employee=employee, salary=salary
            )
            res = {
                'id': employee.id,
                'name': employee.name,
                'alias': employee.alias,
                "salary": salary.salary
            }
            return HttpResponse(json.dumps(res, indent=4), status=status.HTTP_201_CREATED)
     
    def detail(request, employee_id):
        if request.method == "GET":
            salary=EmployeeSalary.objects.get(employee__id=employee_id)
     
            res = {
                'id': salary.employee.id,
                'name': salary.employee.name,
                'alias': salary.employee.alias,
                "salary": salary.salary
            }
            return HttpResponse(json.dumps(res, indent=4), status=status.HTTP_200_OK)
            
        
        if request.method == "PUT":
            data=json.loads(request.body)
            name=data['name']
            alias=data['alias']
            salary=data["salary"]
            
            employee_salary = EmployeeSalary.objects.get(employee__id=employee_id)
            employee = employee_salary.employee
            
            name=data['name']
            alias=data['alias']
            salary=data["salary"]
            
            employee.name = name
            employee.alias = alias
            employee.save()
     
            employee_salary.salary = salary
            employee_salary.save()
     
            res = {
                "id": employee.id,
                "name": employee.name,
                "alias": employee.alias,
                "salary": employee_salary.salary
            }
            
            return HttpResponse(json.dumps(res, indent=4), status=status.HTTP_202_ACCEPTED)
     
        if request.method == "DELETE":
            employee=Employee.objects.get(id=employee_id)
            employee.delete()
            res = {
                'name': employee.name,
                'alias': employee.alias,
            }
            return HttpResponse(json.dumps(res, indent=4), status=status.HTTP_202_ACCEPTED)