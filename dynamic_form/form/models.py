from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django import forms


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Survey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seen_brands = models.ManyToManyField(Brand)
    produse_brands = models.ManyToManyField(Brand, related_name="seen_brands")
    pastuse_brands = models.ManyToManyField(Brand, related_name="produse_brands")
    ad_blocking = models.BooleanField()
    yt_sub = models.BooleanField()


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ["seen_brands", "ad_blocking"]
        widgets = {
            "seen_brands": forms.CheckboxSelectMultiple,
            "produse_brands": forms.CheckboxSelectMultiple,
            "pastuse_brands": forms.CheckboxSelectMultiple,
            "ad_blocking": forms.CheckboxInput,
            "yt_sub": forms.CheckboxInput,
        }
        labels = {
            "seen_brands": "I remember seeing ads for the following brands this year",
            "produse_brands": "I remember using products of the following brands this year",
            "pastuse_brands": "I have used these brands at least once in the past",
            "ad_blocking": "I use ad blocking software",
            "yt_sub": "Do you use a Youtube subscription?",
        }
