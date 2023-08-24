from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.employee.models import Employee

from .serializer import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('last_name', 'department',)

    @action(methods=['get'], detail=False, url_path='department/(?P<department_pk>[^/.]+)')
    def filter_by_department(self, request, department_pk):
        query_set = super().get_queryset().filter(department=department_pk)
        if not query_set:
            raise Http404
        result = self.get_serializer(data=query_set, many=True)
        result.is_valid()
        return Response(result.data, status=status.HTTP_200_OK)
