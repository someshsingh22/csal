from django.urls import path, include
from .views import intro_survey

urlpatterns = [
    path("", intro_survey, name="intro_survey"),
]
