from rest_framework import serializers

from apps.employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'last_name',
            'first_name',
            'surname',
            'photo',
            'job_title',
            'salary',
            'birthday',
            'department',
        )
