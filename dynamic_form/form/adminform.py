from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .questions import Video, Experience


class HiddenSurvey(models.Model):
    video = models.ManyToManyField(Video)
    ad_seen = models.BooleanField()
    brand_ads_seen = models.BooleanField()
    brand_heard = models.BooleanField()


class SelectUserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Select the user")


class HiddenSurveyForm(forms.ModelForm):
    video = forms.ModelChoiceField(
        queryset=Video.objects.all(), label="Select the video"
    )

    ad_seen = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Have you seen the ad before?",
    )
    brand_ads_seen = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Have you seen any ad from that brand before?",
    )
    brand_heard = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Have you heard about that brand before?",
    )

    class Meta:
        model = HiddenSurvey
        fields = ["video", "ad_seen", "brand_ads_seen", "brand_heard"]
        widgets = {
            "ad_seen": forms.TypedChoiceField,
            "brand_ads_seen": forms.TypedChoiceField,
            "brand_heard": forms.TypedChoiceField,
        }


def hidden_user(request):
    if request.user != User.objects.get(username="someshs"):
        return render(request, "error.html")
    if request.method == "POST":
        form = SelectUserForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data["user"].id
            return redirect(f"/form/hidden_survey/?user={user_id}")
        else:
            return render(request, "hidden_user.html", {"form": form})

    else:
        form = SelectUserForm()
        return render(request, "hidden_user.html", {"form": form})


def hidden_survey(request):
    if request.user != User.objects.get(username="someshs"):
        return render(request, "error.html")

    if request.method == "POST":
        form = HiddenSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "ask.html")
        else:
            return render(request, "error.html")

    else:
        try:
            user_id = request.GET.get("user")
        except:
            return render(request, "error.html")
        user = User.objects.get(id=user_id)
        user_videos = Experience.objects.get(user=user_id).videos.all()
        form = HiddenSurveyForm(initial={"user": user})
        form.fields["video"].queryset = user_videos
        return render(request, "hidden_survey.html", {"form": form})
