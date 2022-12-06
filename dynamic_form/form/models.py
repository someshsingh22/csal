from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django import forms


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AppriseMethod(models.Model):
    method = models.CharField(max_length=255)

    def __str__(self):
        return self.method


class Survey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seen_brands = models.ManyToManyField(Brand, related_name="seen")
    produse_brands = models.ManyToManyField(Brand, related_name="produse")
    pastuse_brands = models.ManyToManyField(Brand, related_name="pastuse")
    ad_blocking = models.BooleanField()
    yt_sub = models.BooleanField()
    youtube_percentage = models.IntegerField()
    apprise_methods = models.ManyToManyField(AppriseMethod)


class SurveyForm(forms.ModelForm):
    YOUTUBE_PERCENTAGE_CHOICES = [
        (1, "<10% on mobile"),
        (2, ">10% but <30% on mobile"),
        (3, ">30% but <70% on mobile"),
        (4, ">70% on mobile"),
    ]
    youtube_percentage = forms.ChoiceField(
        choices=YOUTUBE_PERCENTAGE_CHOICES,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Survey
        fields = [
            "seen_brands",
            "produse_brands",
            "pastuse_brands",
            "ad_blocking",
            "yt_sub",
            "youtube_percentage",
            "apprise_methods",
        ]
        widgets = {
            "seen_brands": forms.CheckboxSelectMultiple,
            "produse_brands": forms.CheckboxSelectMultiple,
            "pastuse_brands": forms.CheckboxSelectMultiple,
            "ad_blocking": forms.CheckboxInput,
            "yt_sub": forms.CheckboxInput,
            "apprise_methods": forms.CheckboxSelectMultiple,
        }
        labels = {
            "seen_brands": "I remember seeing ads for the following brands this year",
            "produse_brands": "I remember using products of the following brands this year",
            "pastuse_brands": "I have used these brands at least once in the past",
            "ad_blocking": "I use ad blocking software",
            "yt_sub": "Do you use a Youtube subscription?",
            "nouse_brands": "I have never used these brands",
            "youtube_percentage": "Approximately how much percentage of time do you spend on Youtube mobile vs Youtube web?",
            "apprise_methods": "How do you apprise yourself of the latest products and brands?",
        }
