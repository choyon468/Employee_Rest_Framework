from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated

def home(request):
    return HttpResponse("Hello, rest framework app!")


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAuthenticated]
