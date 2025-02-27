from django.shortcuts import render, HttpResponse

#Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#Model
from .models import Company
#Serializer
from .serializers import CompanySerializer



# Create your views here.

def home(request):
    return HttpResponse("olá")

@api_view(['GET'])
def companies(request):
    companies = Company.objects.all()
    companies_serialized = CompanySerializer(companies,many=True)
    return Response(companies_serialized.data,status=status.HTTP_200_OK)

