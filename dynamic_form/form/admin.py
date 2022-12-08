from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import tablib, json

from .intro import Brand, AppriseMethod, SeenBrands, ProdUseBrands, PastUseBrands
from .questions import Video, Experience, Emotions, BrandOptions
from .stage import UserStage


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


class SeenBrandsResource(resources.ModelResource):
    class Meta:
        model = SeenBrands


class ProdUseBrandsResource(resources.ModelResource):
    class Meta:
        model = ProdUseBrands


class PastUseBrandsResource(resources.ModelResource):
    class Meta:
        model = PastUseBrands


class BrandOptionsResource(resources.ModelResource):
    class Meta:
        model = BrandOptions


class UserStageResource(resources.ModelResource):
    class Meta:
        model = UserStage


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


class SeenBrandsAdmin(ImportExportModelAdmin):
    resource_class = SeenBrandsResource


class ProdUseBrandsAdmin(ImportExportModelAdmin):
    resource_class = ProdUseBrandsResource


class PastUseBrandsAdmin(ImportExportModelAdmin):
    resource_class = PastUseBrandsResource


class BrandOptionsAdmin(ImportExportModelAdmin):
    resource_class = BrandOptionsResource


class UserStageAdmin(ImportExportModelAdmin):
    resource_class = UserStageResource


for model_name, admin_name, resource, file_name in zip(
    [
        Brand,
        AppriseMethod,
        Video,
        Experience,
        Emotions,
        SeenBrands,
        ProdUseBrands,
        PastUseBrands,
        BrandOptions,
        UserStage,
    ],
    [
        BrandAdmin,
        AppriseMethodAdmin,
        VideoAdmin,
        ExperienceAdmin,
        EmotionsAdmin,
        SeenBrandsAdmin,
        ProdUseBrandsAdmin,
        PastUseBrandsAdmin,
        BrandOptionsAdmin,
        UserStageAdmin,
    ],
):
    admin.site.register(model_name, admin_name)


for resource, file_name in zip(
    [
        BrandResource,
        AppriseMethodResource,
        VideoResource,
        ExperienceResource,
        EmotionsResource,
        SeenBrandsResource,
        ProdUseBrandsResource,
        PastUseBrandsResource,
        BrandOptionsResource,
        UserStageResource,
    ],
    [
        "brand",
        "apprise_method",
        "video",
        "experience",
        "emotions",
        "seen_brands",
        "produse_brands",
        "pastuse_brands",
        "brand_options",
        "user_stage",
    ],
):
    dataset = tablib.Dataset().load(open(f"data/{file_name}.json"), format="json")
    resource().import_data(dataset, dry_run=False)
