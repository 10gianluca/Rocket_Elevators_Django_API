from rest_framework import serializers
from base.models import Employees

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id','firstname','lastname','title','email', 'password', 'updated_at','created_at','facial_keypoints')