import logging

from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .intro import Brand

logging.basicConfig(level=logging.INFO, filename="debug.log")


class Video(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    path = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    watchset = models.IntegerField()

    def __str__(self):
        return self.path


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Video)

    def __str__(self):
        return (
            f"User:{self.user}:{','.join([str(video) for video in self.videos.all()])}"
        )


class BrandOptions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brands = models.ManyToManyField(Brand)


class RememberedBrand(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    scenes_description = models.TextField()
    audio = models.IntegerField()
    usage_product = models.IntegerField()
    used_brand = models.BooleanField()
    ad_seen = models.BooleanField()

    def __str__(self):
        return f"User:{self.experience.user}:{self.brand}"


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
            "audio",
            "usage_product",
            "used_brand",
            "ad_seen",
        ]
        widgets = {
            "experience": forms.HiddenInput,
            "brand": forms.HiddenInput,
            "scenes_description": forms.Textarea,
        }
        labels = {
            "scenes_description": f"For this brand's ad, I remember seeing the following (Write Scene Descriptions)",
        }


def brand_survey(request):
    if not OverallQuestionSurvey.objects.filter(exp__user=request.user).exists():
        return redirect("/form/overall")

    if not request.GET.get("page"):
        try:
            return redirect("/form/brand?page=1")
        except IndexError:
            return render(request, "error.html", {"message": "No brands to survey"})

    curr_page = int(request.GET.get("page"))

    survey = OverallQuestionSurvey.objects.get(exp__user=request.user)
    brands = survey.remembered_brands.all()

    if curr_page > len(brands):
        return render(request, "thankyou.html")

    if RememberedBrand.objects.filter(
        experience__user=request.user,
        brand=brands[curr_page - 1],
    ).exists():
        return redirect("/form/brand?page={}".format(curr_page + 1))

    if request.method == "POST":
        form = RememberedBrandForm(request.POST)
        if form.is_valid():
            form.save()
            next_page = curr_page + 1
            return redirect("/form/brand?page={}".format(next_page))
        else:
            return redirect("/form/brand?page={}".format(curr_page))
    else:
        brand = brands[curr_page - 1].name
        curr_form = RememberedBrandForm(
            initial={
                "experience": Experience.objects.get(user=request.user).id,
                "brand": brands[curr_page - 1].id,
            }
        )
        for field in curr_form.fields:
            curr_form.fields[field].label = curr_form.fields[field].label.replace(
                "this brand", brand
            )
        return render(request, "brand_survey.html", {"form": curr_form, "brand": brand})


class OverallQuestionSurvey(models.Model):
    exp = models.ForeignKey(Experience, on_delete=models.CASCADE)
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


def overall_survey(request):
    if OverallQuestionSurvey.objects.filter(exp__user=request.user).exists():
        return redirect("/form/brand?page=1")

    if request.method == "POST":
        form = OverallQuestionSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/form/brand?page=1")
        else:
            return render(request, "short_term.html", {"form": form})
    else:
        exp = Experience.objects.get(user=request.user)
        form = OverallQuestionSurveyForm(initial={"exp": exp})
        form.fields["remembered_brands"].queryset = BrandOptions.objects.get(
            user=request.user
        ).brands.all()
        return render(request, "short_term.html", {"form": form})
