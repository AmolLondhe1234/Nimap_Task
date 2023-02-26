from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators  import api_view
from rest_framework.views import APIView
from rest_framework.generics import *
from .models import *
from .serializer import *
from rest_framework.response import Response
from user.serializer  import *
from rest_framework.parsers import JSONParser
# Create your views here.


class clientlist(ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    def post(self,request):
        serializer=ClientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

# @api_view(['GET','POST'])
# def clientlist(request):
#     if request.method == 'GET':
#         transformer = Client.objects.all()
#         serializer = ClientSerializer(transformer, many=True)
#         return Response(serializer.data)
  
#     elif request.method == 'POST':
#         data = Client.objects.all()
#         serializer = ClientSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    

class clientup(RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

class projectlist(ListCreateAPIView):
    queryset=ClientP.objects.all()
    serializer_class=ClientPSerializer
    # def post(self,request):
    #     serializer=ProjectSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()

    #     return Response(serializer.data)

# @api_view(['POST'])
# def projectcreate(request):
#     serializer=ProjectSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)