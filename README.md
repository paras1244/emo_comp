
# IDEA
Get Child Models Details From Parent Model

# Description

# Models
I have created 3 models (Company, Departments, Employee)
I have Used ""unique_together"" on Department and Employee model Accoringly. 
I have Write ""related_name"" When I Write the relationship of model(Foreignkeys) 

# Views
I have used ""APIView"" and ""ModelViewSet"" to create the API accordingly

# serializers 
I have created Serializers to Get Details of Employee Directly with Company Details
1) Using depth = 1
2) using Simpe "serializers.SerializerMethodField" Method

# API : Get All Company and Relevent Department-Employee Details.
http://127.0.0.1:8000/company/*

# Retrive Company Details Along With Department-Employee
http://127.0.0.1:8000/company/1/
Please check the  ""postman_collection.json"" file for Examples,


# Published Postman documentation Link &  Exported JSON File
https://documenter.getpostman.com/view/19442321/UzXKVy2Q

#### I have saved Each API's Example in here ####
related_path : Latitude Test.postman_collection.json



# Steps To Set-up The Project 
git clone https://github.com/paras1244/emp_comp.git
