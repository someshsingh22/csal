from django.forms import modelformset_factory
from django.shortcuts import render
from .models import IntroductoryQuestionnaire
from django.contrib.auth.decorators import login_required

@login_required
def introduction(request):
    IntroductoryQuestionnaireFormSet = modelformset_factory(IntroductoryQuestionnaire, exclude=("user",))
    if request.method == 'POST':
        formset = IntroductoryQuestionnaireFormSet(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = IntroductoryQuestionnaireFormSet()
    return render(request, 'introduction.html', {'formset': formset})