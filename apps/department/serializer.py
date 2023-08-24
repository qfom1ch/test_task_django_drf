from rest_framework import serializers

from apps.department.models import Department
from apps.employee.serializer import EmployeeSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    director = EmployeeSerializer()
    employees_count = serializers.IntegerField()
    salary_sum = serializers.IntegerField()

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'director',
            'employees_count',
            'salary_sum',
        )
