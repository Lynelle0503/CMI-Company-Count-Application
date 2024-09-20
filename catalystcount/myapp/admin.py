from django.contrib import admin
from .models import CompanyData
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(CompanyData)
class CompanyDataAdmin(ImportExportModelAdmin):
    list_display = ('name', 'domain', 'founded_year')
