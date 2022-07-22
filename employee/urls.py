
from django.urls import path
from .views import CompanyView, DepartmentsView, EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'company', CompanyView)

urlpatterns = [
    path('department/', DepartmentsView.as_view(), name='departments'),
]

urlpatterns += router.urls