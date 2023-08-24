from django.urls import include, path
from rest_framework import routers

from .views import EmployeeViewSet

app_name = 'employee'

router = routers.SimpleRouter()
router.register(r'', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls), name='employee'),
]
