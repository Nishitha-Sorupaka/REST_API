from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import *
from rest_framework.viewsets import ViewSet
# Create your views here.
class TestViewSet(ViewSet):
    def list(self, request):
        colors = ['RED', 'YELLOW', 'GREEN', 'WHITE', 'PINK']
        return Response({'msg': 'Happy Weekend', 'colors': colors})

    def create(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {} Happy Weekend'.format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errors, status=400)
    def retrieve(self, request, pk=None):
        return Response({'msg': 'This response from RETRIEVE method of ViewSet'})
    def update(self, request, pk=None):
        return Response({'msg': 'This response from UPDATE method of ViewSet'})
    def partial_update(self, request, pk=None):
        return Response({'msg': 'This response from PARTIAL UPDATE method of ViewSet'})
    def destroy(self, request, pk=None):
        return Response({'msg': 'This response from DESTROY method of ViewSet'})

class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ['RED','YELLOW','GREEN','BLUE','PINK']
        return Response({'msg': 'Happy Weekend','colors':colors}) #Response class is responsible to convert python_dict to json_data

    def post(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {} Happy Weekend'.format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        return Response({'msg': 'This response is from put method APIView'})

    def patch(self, request, *args, **kwargs):
        return Response({'msg': 'This response is from patch method APIView'})

    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'This response is from delete method APIView'})