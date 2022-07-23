
from .models import Company, Departments, Employee
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import CompanySerializer, DepartmentsSerializer, EmployeeSerializer
from django.db.models import Count

class DepartmentsView(APIView):

    def get(self, request):
        departments = Departments.objects.all()
        serialize = DepartmentsSerializer(departments, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = DepartmentsSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
    

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     print(" retrieve called >>>>>>>>>> ", self.get_object().id)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
    
    
    # Country.objects.all().values("id","country_name").annotate(total_customer=Count(customer_country))    
    """
    # instance2 = Company.objects.filter(id = self.get_object().id) \
        .values("company_name", "city") \
        .annotate(total_emp=Count('employee_company'))
    
    SELECT "employee_company"."company_name", "employee_company"."city",
        COUNT("employee_employee"."id") AS "total_emp" 
            FROM "employee_company" LEFT OUTER JOIN "employee_employee"
                ON ("employee_company"."id" = "employee_employee"."company_id")
                    WHERE "employee_company"."id" = 1 
                        GROUP BY "employee_company"."company_name", "employee_company"."city"
    """
    
    
    """
    instance2 = Company.objects.filter(id = self.get_object().id).annotate(total_emp=Count('employee_company'))
    
        SELECT "employee_company"."id", 
        "employee_company"."company_name",
        "employee_company"."city",
        "employee_company"."created_at",
        "employee_company"."updated_at",
            COUNT("employee_employee"."id") AS "total_emp" 
                FROM "employee_company"
                    LEFT OUTER JOIN "employee_employee" 
                        ON ("employee_company"."id" = "employee_employee"."company_id") 
                            WHERE "employee_company"."id" = 1 
                                GROUP BY "employee_company"."id",
                                    "employee_company"."company_name",
                                    "employee_company"."city", 
                                    "employee_company"."created_at",
                                    "employee_company"."updated_at"
    """
    
    
    """ 
    instance2 = Company.objects.filter(id = self.get_object().id) \
                .values("employee_company") \
                .annotate(total_emp=Count('employee_company'))
    
    SELECT "employee_employee"."id",
        COUNT("employee_employee"."id") AS "total_emp"
            FROM "employee_company" 
                LEFT OUTER JOIN "employee_employee" 
                    ON ("employee_company"."id" = "employee_employee"."company_id")
                        WHERE "employee_company"."id" = 1 
                            GROUP BY "employee_employee"."id"
    """