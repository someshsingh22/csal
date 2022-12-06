from django.contrib import admin

from .models import Brand, AppriseMethod
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand


class AppriseMethodResource(resources.ModelResource):
    class Meta:
        model = AppriseMethod


class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource


class AppriseMethodAdmin(ImportExportModelAdmin):
    resource_class = AppriseMethodResource


admin.site.register(Brand, BrandAdmin)
admin.site.register(AppriseMethod, AppriseMethodAdmin)
