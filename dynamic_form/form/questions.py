import logging
import random
from collections import OrderedDict

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


class BrandOptions(models.Model):
    exp = models.ForeignKey(Experience, on_delete=models.CASCADE)
    brands = models.ManyToManyField(Brand)


class RememberedBrand(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    scenes_description = models.TextField()
    audio = models.IntegerField()
    usage_product = models.IntegerField()
    used_brand = models.BooleanField()
    ad_seen = models.BooleanField()
    attention_check = models.CharField(max_length=256)
    attention_check_answer = models.IntegerField()

    def __str__(self):
        return f"User:{self.experience.user}:{self.brand}"


questions = [
    "I am paid bi-weekly by leprechauns",
    "In the last one year, I have suffered from congenital parantoscopy",
    "I know that people have to pay brands to advertise brand’s products",
    "I have never used a computer",
    "What is the sum of 5 and 7?",
    "What is the result of 6 multiplied by 9?",
    "The Apple brand which manufactures iPhones is a sub-brand of the Google and Facebook brands",
    "How many times have you written the gospel of ghost and the demon in the cognitive science course this year?",
    "If I could, I would want to pass the cognitive science course:",
    "The founders of brands Apple, Google, Facebook, PayTM, Maruti, Dell, and Toyota are of Pakistani origin:",
    "All brands congregate at the North Pole on the New Year’s eve and stop their advertising for one day:",
]

choices = [
    ["Disagree", "Agree"],
    ["0 times", "1-2 times", "3-10 times", "10+ times"],
    ["Disagree", "Agree"],
    ["Agree", "Disagree"],
    ["10", "11", "12", "13"],
    ["54", "63", "42", "36"],
    ["Agree", "Disagree"],
    ["0", "1-10", "10+"],
    ["Agree", "Disagree"],
    ["Agree", "Disagree"],
    ["Agree", "Disagree"],
]


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

    attention_check_answer = forms.ChoiceField(
        widget=forms.RadioSelect,
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
            "attention_check",
            "attention_check_answer",
        ]
        widgets = {
            "experience": forms.HiddenInput,
            "brand": forms.HiddenInput,
            "attention_check": forms.HiddenInput,
            "scenes_description": forms.Textarea,
        }
        labels = {
            "scenes_description": f"For this brand's ad, I remember seeing the following (Write Scene Descriptions)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        q_no = random.randint(0, len(questions) - 1)
        question, options = questions[q_no], choices[q_no]
        self.fields["attention_check"].initial = question
        self.fields["attention_check_answer"].label = question
        self.fields["attention_check_answer"].choices = [
            (i + 1, option) for i, option in enumerate(options)
        ]


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
            logging.error(form.errors)
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
            if field not in ["attention_check", "attention_check_answer"]:
                curr_form.fields[field].label = curr_form.fields[field].label.replace(
                    "this brand", brand
                )
        fields = list(curr_form.fields)
        total_fields = len(fields)
        fields.insert(
            random.randint(total_fields - 3, total_fields), "attention_check_answer"
        )
        curr_form.fields = OrderedDict(
            (field, curr_form.fields[field]) for field in fields
        )
        return render(request, "brand_survey.html", {"form": curr_form, "brand": brand})


class OverallQuestionSurvey(models.Model):
    exp = models.ForeignKey(Experience, on_delete=models.CASCADE)
    remembered_brands = models.ManyToManyField(Brand)
    for sector in SECTORS:
        locals()[f"{sector}_seen"] = models.BooleanField()


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
            labels[f"{sector}_seen"] = sector


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
