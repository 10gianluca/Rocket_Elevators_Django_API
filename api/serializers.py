from rest_framework import serializers
from base.models import Employees

class Employees(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'