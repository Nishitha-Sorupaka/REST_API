from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def emp_data_view(request):
    emp_data = {
        'eno':101,'ename':'sunny','esal':15000,'eaddr':'Chennai'
    }
    resp = '<h1>Employee Number: {}<br>Employee Name: {}<br>Employee Salary: {}<br>Employee Address: {}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data = {
        'eno': 101, 'ename': 'sunny', 'esal': 15000, 'eaddr': 'Chennai'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type='application/json')

def emp_data_jsonview2(request):
    emp_data = {
        'eno': 101, 'ename': 'sunny', 'esal': 15000, 'eaddr': 'Chennai'
    }
    return JsonResponse(emp_data)

#class based views
from testapp.mixins import HttpResponseMixin
from django.views.generic import View
class JsonCBV(HttpResponseMixin,View):
    def get(self,request,*args, **kwargs):
        json_data = json.dumps({'msg':'This is from get method'})
        return self.render_to_http_response(json_data)
    def post(self,request,*args, **kwargs):
        json_data = json.dumps({'msg':'This is from post method'})
        return self.render_to_http_response(json_data)
    def put(self,request,*args, **kwargs):
        json_data = json.dumps({'msg':'This is from put method'})
        return self.render_to_http_response(json_data)
    def delete(self,request,*args, **kwargs):
        json_data = json.dumps({'msg':'This is from delete method'})
        return self.render_to_http_response(json_data)

'''
        emp_data = {
            'eno': 103,
            'ename': 'Kareena',
            'esal': 19000,
            'eaddr': 'Delhi',
        }
        return JsonResponse(emp_data)
        '''

