from django.contrib import admin
from study_buddy.classroom.models import Homework, School, Event

# Register your models here.

admin.site.register(Homework)
admin.site.register(School)
admin.site.register(Event)
