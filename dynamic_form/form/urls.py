from django.urls import path, include
from .views import introduction

urlpatterns = [
    path('', introduction, name='introduction'),
]