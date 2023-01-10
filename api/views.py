from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Employees
from .serializers import EmployeesSerializer

@api_view(['GET'])
def getData(request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addEmployee(request):
    serializer = EmployeesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return  Response(serializer.data)