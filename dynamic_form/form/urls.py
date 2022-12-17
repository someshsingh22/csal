from django.urls import path, include
from .intro import intro_survey
from .questions import overall_survey, brand_survey
from .adminform import hidden_survey, hidden_user
from .short_questions import overall_survey_l, brand_survey_l
from .status import user_status

urlpatterns = [
    path("", intro_survey, name="intro_survey"),
    path("overall/", overall_survey, name="overall_survey"),
    path("brand/", brand_survey, name="brand_survey"),
    path("hidden_user/", hidden_user, name="hidden_user"),
    path("hidden_survey/", hidden_survey, name="hidden_survey"),
    path("l_overall/", overall_survey_l, name="overall_survey"),
    path("l_brand/", brand_survey_l, name="brand_survey"),
    path("status", user_status, name="Status")
]
