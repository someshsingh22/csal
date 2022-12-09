from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .intro import Brand, AppriseMethod
from .questions import Video, Experience, Emotions


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


class EmotionsResource(resources.ModelResource):
    class Meta:
        model = Emotions


class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource


class AppriseMethodAdmin(ImportExportModelAdmin):
    resource_class = AppriseMethodResource


class VideoAdmin(ImportExportModelAdmin):
    resource_class = VideoResource


class ExperienceAdmin(ImportExportModelAdmin):
    resource_class = ExperienceResource


class EmotionsAdmin(ImportExportModelAdmin):
    resource_class = EmotionsResource


for model_name, admin_name in zip(
    [Brand, AppriseMethod, Video, Experience, Emotions],
    [BrandAdmin, AppriseMethodAdmin, VideoAdmin, ExperienceAdmin, EmotionsAdmin],
):
    admin.site.register(model_name, admin_name)
