import json

from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

SECTORS = json.load(open("data/sectors.json"))
NUM_BRAND_PRODUCT_OPTIONS = 3
NUM_OPTIONS = 15


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
    gpa = models.FloatField(
        validators=[MinValueValidator(4.0), MaxValueValidator(10.0)]
    )
    for sector in SECTORS:
        for option in range(NUM_BRAND_PRODUCT_OPTIONS):
            locals()[f"brand_{sector}_{option}"] = models.CharField(
                max_length=255, blank=True, default=""
            )
            locals()[f"product_{sector}_{option}"] = models.CharField(
                max_length=255, blank=False, null=False
            )


class SeenBrands(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seen_brands = models.ManyToManyField(Brand)


class ProdUseBrands(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    produse_brands = models.ManyToManyField(Brand)


class PastUseBrands(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pastuse_brands = models.ManyToManyField(Brand)


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

    ad_blocking = forms.TypedChoiceField(
        coerce=lambda x: x == "True", choices=((False, "No"), (True, "Yes"))
    )
    yt_sub = forms.TypedChoiceField(
        coerce=lambda x: x == "True", choices=((False, "No"), (True, "Yes"))
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
            "gpa",
        ]
        widgets = {
            "user": forms.HiddenInput,
            "seen_brands": forms.CheckboxSelectMultiple,
            "produse_brands": forms.CheckboxSelectMultiple,
            "pastuse_brands": forms.CheckboxSelectMultiple,
            "apprise_methods": forms.CheckboxSelectMultiple,
        }
        labels = {
            "seen_brands": "I remember seeing ads for the following brands this year",
            "produse_brands": "I remember using products of the following brands this year",
            "pastuse_brands": "I have used these brands at least once in the past",
            "ad_blocking": "I use ad blocking software",
            "yt_sub": "Do you use a Youtube subscription?",
            "youtube_percentage": "Approximately how much percentage of time do you spend on Youtube mobile vs Youtube web?",
            "apprise_methods": "How do you apprise yourself of the latest products and brands?",
            "gpa": "What is your CGPA?",
        }
        for sector in SECTORS:
            for option in range(NUM_BRAND_PRODUCT_OPTIONS):
                fields.append(f"brand_{sector}_{option}")
                fields.append(f"product_{sector}_{option}")

                labels[f"brand_{sector}_{option}"] = "Brand"
                labels[f"product_{sector}_{option}"] = "Product"

                widgets[f"brand_{sector}_{option}"] = forms.TextInput()
                widgets[f"product_{sector}_{option}"] = forms.TextInput()

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not name.startswith("brand_") or name.startswith("product_"):
                # add class to all field labels
                pass


@login_required
def intro_survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thankyou.html")
    else:
        form = SurveyForm(initial={"user": request.user})
        seen_brands = SeenBrands.objects.filter(user=request.user)
        produse_brands = ProdUseBrands.objects.filter(user=request.user)
        pastuse_brands = PastUseBrands.objects.filter(user=request.user)
        form.fields["seen_brands"].queryset = seen_brands
        form.fields["produse_brands"].queryset = produse_brands
        form.fields["pastuse_brands"].queryset = pastuse_brands
    return render(request, "introduction.html", {"form": form})
