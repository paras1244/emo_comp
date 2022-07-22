from django.db import models

# Create your models here.

# Company model with city name
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.company_name


class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, related_name='dep_company', on_delete=models.CASCADE)

    # unique together company and depname
    class Meta:
        unique_together = ('dep_name', 'company')

    def __str__(self):
        return self.dep_name


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='employee_company', on_delete=models.CASCADE)
    
    # Unique Together Emp Dep Cmp
    class Meta:
        unique_together = ("emp_name", "department", "company")

    def __str__(self):
        return self.emp_name

# For Simple Purpose, we need to pass only one FK of Department in Employee Model 