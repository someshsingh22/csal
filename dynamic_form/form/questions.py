from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import logging
import json

logging.basicConfig(level=logging.INFO, filename="debug.log")

from .intro import Brand

RECOGNITION_OPTIONS = 30
SECTORS = json.load(open("data/sectors_prompt.json"))


class Video(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Video)


class Emotions(models.Model):
    emotion = models.CharField(max_length=255)

    def __str__(self):
        return self.emotion


class RememberedBrand(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    scenes_description = models.TextField()
    emotions = models.ManyToManyField(Emotions)
    seen_objects = models.TextField()
    audio = models.IntegerField()
    caption = models.TextField()
    used_brand = models.BooleanField()
    used_product = models.BooleanField()
    usage_brand = models.IntegerField()
    usage_product = models.IntegerField()
    brand_ads_seen = models.BooleanField()
    ad_seen = models.BooleanField()


class RememberedBrandForm(forms.ModelForm):
    AUDIO_CHOICES = [
        (1, "Narration"),
        (2, "Some background music"),
        (3, "No music"),
        (4, "Don't remember"),
    ]

    FREQUENCY_CHOICES = [
        (1, "Never"),
        (2, "1-10"),
        (3, ">10"),
    ]

    audio = forms.ChoiceField(
        choices=AUDIO_CHOICES,
        widget=forms.RadioSelect,
        label="For this brand's ad, I remember hearing the following audio types",
    )

    usage_brand = forms.ChoiceField(
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect,
        label="How many times in the last year have you used the product shown in this brand's ad?",
    )

    usage_product = forms.ChoiceField(
        choices=FREQUENCY_CHOICES,
        widget=forms.RadioSelect,
        label="How many times in the last year have you used this brand?",
    )

    used_brand = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Have you ever used this brand before?",
    )

    used_product = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Have you ever used the product shown in this brand's ad before?",
    )

    brand_ads_seen = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Have you ever seen any advertisements from this brand before?",
    )

    ad_seen = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Have you ever seen this particular advertisement before?",
    )

    class Meta:
        model = RememberedBrand
        fields = [
            "experience",
            "brand",
            "scenes_description",
            "emotions",
            "seen_objects",
            "audio",
            "caption",
            "used_brand",
            "used_product",
            "usage_brand",
            "usage_product",
            "brand_ads_seen",
            "ad_seen",
        ]
        widgets = {
            "experience": forms.HiddenInput,
            "brand": forms.HiddenInput,
            "used_product": forms.CheckboxInput,
            "used_brand": forms.CheckboxInput,
            "brand_ads_seen": forms.CheckboxInput,
            "ad_seen": forms.CheckboxInput,
            "emotions": forms.CheckboxSelectMultiple,
            "audio": forms.RadioSelect,
        }
        labels = {
            "scenes_description": f"For this brand's ad, I remember seeing the following (Write Scene Descriptions)",
            "emotions": "For this brand's ad, I remember feeling these emotion(s)",
            "seen_objects": "For this brand's ad, I remember seeing the following object(s) (Comma Separated)",
            "caption": "Single line caption I would like to give to the ad, i.e I should buy this brand because",
        }


class OverallQuestionSurvey(models.Model):
    exp = models.ForeignKey(Experience, on_delete=models.CASCADE)
    for sector in SECTORS:
        locals()[f"{sector}_seen"] = models.BooleanField()
    remembered_brands = models.ManyToManyField(Brand)


class OverallQuestionSurveyForm(forms.ModelForm):
    class Meta:
        model = OverallQuestionSurvey
        fields = ["exp", "remembered_brands"]
        widgets = {
            "exp": forms.HiddenInput,
            "remembered_brands": forms.CheckboxSelectMultiple,
        }
        labels = {
            "remembered_brands": "In the eye tracking study, I remember seeing Ads of the following brands",
        }
        for sector in SECTORS:
            fields.append(f"{sector}_seen")
            widgets[f"{sector}_seen"] = forms.CheckboxInput
            labels[f"{sector}_seen"] = sector.replace("_", " ")


def overall_survey(request):
    if request.method == "POST":
        form = OverallQuestionSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/form/brand?page=1")
    else:
        exp = Experience.objects.get(user=request.user)
        form = OverallQuestionSurveyForm(initial={"exp": exp})
        videos_seen = exp.videos.all()
        brands_seen = Brand.objects.filter(video__in=videos_seen)
        num_seen_brands = brands_seen.count()
        remaining_brands = Brand.objects.exclude(id__in=brands_seen).order_by("?")
        final_brands = (
            brands_seen | remaining_brands[: RECOGNITION_OPTIONS - num_seen_brands]
        )
        form.fields["remembered_brands"].queryset = final_brands.order_by("?")
    return render(request, "short_term.html", {"form": form})


def brand_survey(request):
    survey = OverallQuestionSurvey.objects.all().filter(exp__user=request.user).last()
    brands = survey.remembered_brands.all()
    exp = Experience.objects.get(user=request.user)
    forms = [
        RememberedBrandForm(initial={"experience": exp, "brand": brand})
        for brand in brands
    ]
    logging.info(len(forms))
    if request.method == "POST":
        form = RememberedBrandForm(request.POST)
        form.save()
        page = request.GET.get("page")
        next_page = int(page) + 1
        return redirect("/form/brand?page={}".format(next_page))
    else:
        page_number = int(request.GET.get("page"))
        brand = brands[page_number - 1].name
        curr_form = forms[page_number - 1]
        return render(request, "brand_survey.html", {"form": curr_form, "brand": brand})
