from django.shortcuts import render
from testapp.models import *
from testapp.serializers import *
from rest_framework.generics import ListAPIView
from testapp.pagination import MyPagination, MyPagination2, MyPagination3

class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination3
    #pagination_class = MyPagination2
    #pagination_class = MyPagination



