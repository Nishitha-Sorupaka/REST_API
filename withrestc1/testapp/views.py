from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import io
from rest_framework.parsers import JSONParser
from testapp.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json', status=200)
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json', status=200)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serialize = EmployeeSerializer(data=pdata)
        if serialize.is_valid():
            serialize.save()
            msg = {'msg': 'Resource created successfully.....'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json', status=200)
        json_data = JSONRenderer().render(serialize.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        serialize = EmployeeSerializer(emp,data=pdata,partial=True)
        if serialize.is_valid():
            serialize.save()
            msg = {'msg': 'Resource updated successfully.....'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json', status=200)
        json_data = JSONRenderer().render(serialize.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg': 'Resource deleted successfully.....'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json', status=200)



