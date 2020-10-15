from datacenter.models import Passcard
from datacenter.models import Visit

from django.utils.timezone import localtime
from django.shortcuts import render

def format_visit_info(visit):
    is_active = visit.passcard.is_active
    is_strange = visit.is_visit_long() or not is_active
    visit_info = {
        "who_entered": visit.passcard.owner_name,
        "entered_at": localtime(visit.entered_at),
        "duration": visit.get_formatted_duration(),
        "is_active": is_active and "OK" or "Неактивен",
        # Столкнулась с ситуацией, когда в хранилище посетитель с истекшим пропуском
        "is_strange": is_strange and "Да" or "Нет",
    }
    return visit_info


def storage_information_view(request):
    current_visits = Visit.objects.filter(leaved_at=None)
    current_visits_info = [format_visit_info(visit) for visit in current_visits]

    context = {
        "non_closed_visits": current_visits_info,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
