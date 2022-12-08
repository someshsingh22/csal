from django.urls import path, include
from .intro import intro_survey
from .questions import overall_survey, brand_survey

urlpatterns = [
    path("", intro_survey, name="intro_survey"),
    path("overall/", overall_survey, name="overall_survey"),
    path("brand/", brand_survey, name="brand_survey"),
]
