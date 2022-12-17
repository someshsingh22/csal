from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .questions import Video, Experience
import logging

logging.basicConfig(level=logging.INFO, filename="debug.log")


class HiddenSurvey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    ad_seen = models.BooleanField()
    brand_ads_seen = models.BooleanField()
    brand_heard = models.BooleanField()
    prod_clear = models.BooleanField()


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
    prod_clear = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=((False, "No"), (True, "Yes")),
        label="Is it clear what product is the ad trying to sell?",
    )

    class Meta:
        model = HiddenSurvey
        fields = ["user", "video", "ad_seen", "brand_ads_seen", "brand_heard", "prod_clear"]
        widgets = {
            "user": forms.HiddenInput,
            "ad_seen": forms.TypedChoiceField,
            "brand_ads_seen": forms.TypedChoiceField,
            "brand_heard": forms.TypedChoiceField,
            "prod_clear": forms.TypedChoiceField,
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
        users = User.objects.all().exclude(username="someshs")
        form.fields["user"].label_from_instance = lambda obj: str(obj.id)+'__'+str(obj.email) + '__' + str(obj.first_name) + str(obj.last_name)
        return render(request, "hidden_user.html", {"form": form})


def hidden_survey(request):
    if request.user != User.objects.get(username="someshs"):
        return render(request, "error.html")

    user_id = request.GET.get("user")
    user = User.objects.get(id=user_id)
    user_videos = Experience.objects.get(user=user).videos.all()

    if HiddenSurvey.objects.filter(user=user).exists():
        completed = HiddenSurvey.objects.filter(user=user)
        video_completed = [i.video for i in completed]
        remaining_videos = user_videos.exclude(id__in=[v.id for v in video_completed])
    else:
        remaining_videos = user_videos

    if request.method == "POST":
        form = HiddenSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            if len(remaining_videos)==0:
                return redirect(f"/admin/")
            else:
                return redirect(f"/form/hidden_survey/?user={user_id}")
        else:
            return render(request, "error.html")

    else:
        form = HiddenSurveyForm(initial={"user": user})
        form.fields["video"].queryset = user_videos
        if len(remaining_videos)==0:
            return redirect(f"/admin/")
        else:
            return render(request, "hidden_survey.html", {"form": form, "remaining_videos": remaining_videos})
