from rest_framework import generics as g
from .serializers import EmployeeSerializer, EmployeeSalarySerializer
from .models import Employee, EmployeeSalary



class EmployeeListView(g.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeSalaryView(g.ListCreateAPIView):
    queryset = EmployeeSalary.objects.all()
    serializer_class = EmployeeSalarySerializer

class EmployeeDetailView(g.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


class EmployeeSalaryDetailView(g.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeSalary.objects.all()
    serializer_class = EmployeeSalarySerializer
    lookup_field = 'id'