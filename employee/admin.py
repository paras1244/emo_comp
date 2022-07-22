from django.contrib import admin
from .models import Company, Departments, Employee
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_name",
        "city",
        "created_at",
        "updated_at",
    )
admin.site.register(Company, CompanyAdmin)


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "dep_name",
        "company",
    )
admin.site.register(Departments, DepartmentsAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "emp_name",
        "department",
        "company",
    )
admin.site.register(Employee, EmployeeAdmin)