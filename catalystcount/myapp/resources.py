from import_export import resources
from .models import CompanyData

class CompanyDataResource(resources.ModelResource):
    class Meta:
        model = CompanyData
        fields = (
            'name',
            'domain',
            'founded_year',
            'industry',
        )
        fields = (
            'name',
            'domain',
            'year founded',
            'industry',
        )