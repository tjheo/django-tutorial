"""
URL configuration for nsheo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularJSONAPIView
)
from employee import views as ev
from employee import drf_views as dv

urlpatterns = [
    path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),

    path('admin/', admin.site.urls),
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('employees', ev.index, name="employee_index"),
    path('employees/<int:employee_id>', ev.detail, name="employee_detail"),

    path("drf-employees", dv.EmployeeListView.as_view(), name="employee"),
    path("drf-employees-salary", dv.EmployeeSalaryView.as_view(), name="employee_salary"),

    path("drf-employees/<id>", dv.EmployeeDetailView.as_view(), name="employee_detail"),
    path("drf-employees-salary/<id>", dv.EmployeeSalaryDetailView.as_view(), name="employee_salary_detail"),
]
