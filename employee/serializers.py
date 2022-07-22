
from rest_framework import serializers
from .models import Company, Departments, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "company_name",
            "city",
            "created_at",
            "updated_at",
            "dep_company",
            "employee_company",
        ]
        depth = 1


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