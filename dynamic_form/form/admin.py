from django.contrib import admin

from .models import Brand
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand


class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource


admin.site.register(Brand, BrandAdmin)
