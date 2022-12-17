from django.shortcuts import render
from .short_questions import OverallQuestionSurvey_L
from .questions import OverallQuestionSurvey


def user_status(request):
    if request.user.is_authenticated:
        if request.user.id > 121:
            message = "You are curremtly in a waitlist, you shall be sent your take home assignment soon"
            re = False
            link = None
        elif request.user.id > 96:
            if OverallQuestionSurvey_L.objects.filter(exp__user=request.user).exists():
                message = "Your assignment is completed!"
                re = False
                link = None
            else:
                message = "You are yet to fill the following form"
                re = True
                link = "https://someshs.pythonanywhere.com/form/l_overall"
        else:
            if OverallQuestionSurvey.objects.filter(exp__user=request.user).exists():
                message = "Your assignment is completed!"
                re = False
                link = None
            else:
                message = "You are yet to fill the following form"
                re = True
                link = "https://someshs.pythonanywhere.com/form/overall"
    else:
        message = "You are not logged in, first login at this link"
        re = True
        link = "https://someshs.pythonanywhere.com/"

    return render(
        request, "status.html", {"message": message, "redirect": re, "link": link}
    )
