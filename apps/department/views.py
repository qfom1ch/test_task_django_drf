from django.db.models import Count, Sum
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.department.models import Department

from .serializer import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.select_related('director').all()
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.prefetch_related(
            'employees'
        ).annotate(
            employees_count=Count('employees__id'),
            salary_sum=Sum('employees__salary')
        )
