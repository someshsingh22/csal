from django.urls import path, include
from .intro import intro_survey
from .questions import overall_survey, brand_survey
from .adminform import hidden_survey, hidden_user

urlpatterns = [
    path("", intro_survey, name="intro_survey"),
    path("overall/", overall_survey, name="overall_survey"),
    path("brand/", brand_survey, name="brand_survey"),
    path("hidden_user/", hidden_user, name="hidden_user"),
    path("hidden_survey/", hidden_survey, name="hidden_survey"),
]
