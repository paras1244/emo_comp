
from .models import Company, Departments, Employee
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import CompanySerializer, DepartmentsSerializer, EmployeeSerializer


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
