from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

def format_visit_info(visit):
    visit_info = {
        "entered_at": visit.entered_at,
        "duration": visit.get_formatted_duration,
        "is_strange": visit.is_visit_long() and "Да" or "Нет"
    }
    return visit_info


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits_info = [format_visit_info(visit) 
        for visit in this_passcard_visits]
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits_info
    }
    return render(request, 'passcard_info.html', context)
