import json

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import logging

logging.basicConfig(level=logging.INFO, filename="log.txt")
SECTORS = json.load(open("data/sectors.json"))


def newstr(self):
    try:
        return self.name + " - " + self.email
    except:
        return User.__str__()


User.__str__ = newstr


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AppriseMethod(models.Model):
    method = models.CharField(max_length=255)

    def __str__(self):
        return self.method


class UserSeen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brands = models.ManyToManyField(Brand)


class UserProduse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brands = models.ManyToManyField(Brand)


class UserPastuse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brands = models.ManyToManyField(Brand)


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
        label="Approximately how much percentage of time do you spend on Youtube mobile vs Youtube web?",
    )

    ad_blocking = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Do you use an ad blocking software?",
    )
    yt_sub = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Do you use a Youtube subscription?",
    )

    class Meta:
        model = Survey
        fields = [
            "user",
            "seen_brands",
            "produse_brands",
            "pastuse_brands",
            "ad_blocking",
            "yt_sub",
            "youtube_percentage",
            "apprise_methods",
        ]
        widgets = {
            "user": forms.HiddenInput,
            "seen_brands": forms.CheckboxSelectMultiple,
            "produse_brands": forms.CheckboxSelectMultiple,
            "pastuse_brands": forms.CheckboxSelectMultiple,
            "ad_blocking": forms.TypedChoiceField,
            "apprise_methods": forms.CheckboxSelectMultiple,
        }
        labels = {
            "seen_brands": "I remember seeing ads for the following brands this year",
            "produse_brands": "I remember using products of the following brands this year",
            "pastuse_brands": "I have used these brands at least once in the past",
            "apprise_methods": "How do you apprise yourself of the latest products and brands?",
        }


@login_required
def intro_survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thankyou.html")
        else:
            return render(request, "introduction.html", {"form": form})

    else:
        form = SurveyForm(initial={"user": request.user})
        form.fields["seen_brands"].queryset = UserSeen.objects.get(
            user=request.user
        ).brands.all()
        form.fields["produse_brands"].queryset = UserProduse.objects.get(
            user=request.user
        ).brands.all()
        form.fields["pastuse_brands"].queryset = UserPastuse.objects.get(
            user=request.user
        ).brands.all()
    return render(request, "introduction.html", {"form": form})
