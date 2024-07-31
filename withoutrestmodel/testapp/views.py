from django.shortcuts import render
from django.views.generic import View
import json
from django.http import HttpResponse,JsonResponse
from testapp.models import *
from testapp.mixins import SerializerMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import *
from testapp.forms import EmployeeForm

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin,SerializerMixin,View):
    def get_object_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp
    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=404)
        pdata = json.loads(data)
        id = pdata.get('id',None)
        if id is not None:
            emp = self.get_object_id(id=id)
            if emp is None:
                json_data = json.dumps({'msg':'The requested resource not availbale with matched id'})
                return self.render_to_http_response(json_data,status=404)
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=404)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=404)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=404)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is None:
            json_data = json.dumps({'msg': 'To perform updation id is mandatory'})
            return self.render_to_http_response(json_data, status=404)
        emp = self.get_object_id(id)
        if emp is None:
            json_data = json.dumps(
                {'msg': 'The requested employee does not exist, not possible to perform update operation.'})
            return self.render_to_http_response(json_data, status=404)
        provided_data = json.loads(data)
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=404)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=404)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is None:
            json_data = json.dumps({'msg': 'To perform Deletion id is mandatory'})
            return self.render_to_http_response(json_data, status=404)
        emp = self.get_object_id(id)
        if emp is None:
            json_data = json.dumps(
                {'msg': 'The requested employee does not exist, not possible to perform delete operation.'})
            return self.render_to_http_response(json_data, status=404)
        status, deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg': 'Resource deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg': 'Unable to Delete Resource'})
        return self.render_to_http_response(json_data)




class EmployeeDetailCBV(View):
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.get(id=3)
        emp_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data, content_type='application/json')

class EmployeeDetailCBV2(View):
    def get(self, request,id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        emp_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data, content_type='application/json')

from django.core.serializers import serialize
class EmployeeDetailCBV3(View):
    def get(self, request,id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        json_data = serialize('json', [emp,],fields=['eno','ename','eaddr'])
        return HttpResponse(json_data, content_type='application/json')

#To get all records

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetailCBV4(HttpResponseMixin,SerializerMixin,View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')
        #return JsonResponse(json_data, safe=False)
    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=404)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=404)

        #json_data = json.dumps({'msg':'You provided valid json data only'})
        #return self.render_to_http_response(json_data)

        #json_data = json.dumps({'msg':'This is from post method'})
        #return self.render_to_http_response(json_data)

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetailCBV5(HttpResponseMixin,SerializerMixin,View):
    def get(self, request,id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested employee does not exist.'})
            return self.render_to_http_response(json_data,status=404)
            #return HttpResponse(json_data, content_type='application/json', status=404)
        else:
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)
        #return HttpResponse(json_data, content_type='application/json',status=200)
    def get_object_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp
    def put(self, request,id, *args, **kwargs):
        emp = self.get_object_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'The requested employee does not exist, not possible to perform update operation.'})
            return self.render_to_http_response(json_data,status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=404)
        provided_data = json.loads(data)
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=404)

    def delete(self, request,id, *args, **kwargs):
        emp = self.get_object_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'The requested employee does not exist. Not possible to perform delete operation.'})
            return self.render_to_http_response(json_data,status=404)
        #t = emp.delete()#the return type of t is tuple
        #print(t)
        status,deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg':'Resource deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg': 'Unable to Delete Resource'})
        return self.render_to_http_response(json_data)

    '''
    def get(self, request,id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        json_data = self.serialize([emp,])
        return HttpResponse(json_data, content_type='application/json')
    '''