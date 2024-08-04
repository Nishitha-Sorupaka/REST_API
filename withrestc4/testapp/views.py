from django.shortcuts import render
from testapp.models import Employee
from rest_framework.viewsets import ModelViewSet
from testapp.serializers import EmployeeSerializer
# Create your views here.
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
class EmployeeCRUDViewSetCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]