from django.db import models
from django.contrib.auth.models import User


class UserStage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    short_stage = models.BooleanField()
    long_stage = models.BooleanField()
