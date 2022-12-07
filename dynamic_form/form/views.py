import random
import json
from django.shortcuts import render
from .models import Brand, SurveyForm
from django.contrib.auth.decorators import login_required

import logging

NUM_OPTIONS = 15
SECTORS = json.load(open("data/sectors.json"))


@login_required
def intro_survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thankyou.html")
    else:
        form = SurveyForm(initial={"user": request.user})
        sampling = ["seen_brands", "produse_brands", "pastuse_brands"]
        randoms = Brand.objects.order_by("?")[: NUM_OPTIONS * len(sampling)]
        logging.debug(vars(form.fields["seen_brands"]))
        for i, field in enumerate(sampling):
            form.fields[field].queryset = randoms[
                i * NUM_OPTIONS : (i + 1) * NUM_OPTIONS
            ]
    return render(request, "introduction.html", {"form": form, "sectors": SECTORS})
