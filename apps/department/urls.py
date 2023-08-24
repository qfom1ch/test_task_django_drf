from django.urls import include, path
from rest_framework import routers

from .views import DepartmentViewSet

app_name = 'department'

router = routers.SimpleRouter()
router.register(r'', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls), name='department'),
]
