from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .intro import Brand, AppriseMethod, UserProduse, UserSeen
from .questions import Video, Experience, BrandOptions


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand


class AppriseMethodResource(resources.ModelResource):
    class Meta:
        model = AppriseMethod


class UserProduseResource(resources.ModelResource):
    class Meta:
        model = UserProduse


class UserSeenResource(resources.ModelResource):
    class Meta:
        model = UserSeen


class VideoResource(resources.ModelResource):
    class Meta:
        model = Video


class ExperienceResource(resources.ModelResource):
    class Meta:
        model = Experience


class BrandOptionsResource(resources.ModelResource):
    class Meta:
        model = BrandOptions


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


class UserProduseAdmin(ImportExportModelAdmin):
    resource_class = UserProduseResource


class UserSeenAdmin(ImportExportModelAdmin):
    resource_class = UserSeenResource


class VideoAdmin(ImportExportModelAdmin):
    resource_class = VideoResource


class ExperienceAdmin(ImportExportModelAdmin):
    resource_class = ExperienceResource


class BrandOptionsAdmin(ImportExportModelAdmin):
    resource_class = BrandOptionsResource


for model_name, admin_name in zip(
    [
        Brand,
        AppriseMethod,
        UserProduse,
        UserSeen,
        Video,
        Experience,
        BrandOptions,
    ],
    [
        BrandAdmin,
        AppriseMethodAdmin,
        UserProduseAdmin,
        UserSeenAdmin,
        VideoAdmin,
        ExperienceAdmin,
        BrandOptionsAdmin,
    ],
):
    admin.site.register(model_name, admin_name)
