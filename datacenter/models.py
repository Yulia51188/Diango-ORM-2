from datetime import timedelta
from django.utils.timezone import localtime
from django.db import models

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        time_in = localtime(self.entered_at)
        time_out = localtime(self.leaved_at) or localtime()
        duration = time_out - time_in
        return duration.total_seconds()

    def is_visit_long(self, minutes_limit=60):
        duration = self.get_duration()
        seconds_limit = minutes_limit * 60
        return duration > seconds_limit

    def get_formatted_duration(self):
        total_seconds = self.get_duration()
        hours = total_seconds // 3600
        minutes = total_seconds % 3600 // 60
        seconds = total_seconds % 3600 % 60
        return f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"


