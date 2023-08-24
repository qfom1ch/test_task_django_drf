from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'department', 'age',)
    list_filter = ('department',)
    search_fields = ('first_name', 'last_name', 'surname',)
