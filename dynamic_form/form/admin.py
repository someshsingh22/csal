from django.contrib import admin

from .models import Brand, AppriseMethod, Video, Experience
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand


class AppriseMethodResource(resources.ModelResource):
    class Meta:
        model = AppriseMethod


class VideoResource(resources.ModelResource):
    class Meta:
        model = Video


class ExperienceResource(resources.ModelResource):
    class Meta:
        model = Experience


class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource


class AppriseMethodAdmin(ImportExportModelAdmin):
    resource_class = AppriseMethodResource


class VideoAdmin(ImportExportModelAdmin):
    resource_class = VideoResource


class ExperienceAdmin(ImportExportModelAdmin):
    resource_class = ExperienceResource


for model_name, admin_name in zip(
    [Brand, AppriseMethod, Video, Experience],
    [BrandAdmin, AppriseMethodAdmin, VideoAdmin, ExperienceAdmin],
):
    admin.site.register(model_name, admin_name)
