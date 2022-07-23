
from rest_framework import serializers
from .models import Company, Departments, Employee


class CompanySerializer(serializers.ModelSerializer):
    total_dep = serializers.SerializerMethodField()
    total_emp = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = [
            "id",
            "company_name",
            "city",
            "created_at",
            "updated_at",
            "dep_company",                     # related_name argument
            "employee_company",                 # related_name argument
            "total_dep",
            "total_emp",
        ]
        depth = 1
        
    def get_total_dep(self, object):
        return object.dep_company.all().count()                              # Using Related name
        # return Departments.objects.filter(company=object).count()              # With direct filteting on Employee

    def get_total_emp(self, object):
        # return object.employee_company.all().count()                      # Using Related name
        return Employee.objects.filter(company=object).count()              # With direct filteting on Employee
    

# # TODO : ALSO WE CAN DO LIKE THIS
# class CompanySerializer(serializers.ModelSerializer):
#     departments = serializers.SerializerMethodField()
#     employee = serializers.SerializerMethodField()
#     class Meta:
#         model = Company
#         fields = [
#             "id",
#             "company_name",
#             "city",
#             "created_at",
#             "updated_at",
#             "departments",
#             "employee",
#         ]

#     # Fetching Departments of Self (company object)
#     def get_departments(self, object):
#         return DepartmentsSerializer(object.dep_company.all(), many=True).data
    
#     # Fetching Employees of Self (company object)
#     def get_employee(self, object):
#         return EmployeeSerializer(object.employee_company.all(), many=True).data


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = [
            "id",
            "dep_name",
            "company",
        ]
        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "emp_name",
            "department",
            "company",
        ]