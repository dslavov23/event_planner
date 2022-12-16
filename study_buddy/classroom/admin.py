from django.contrib import admin
from study_buddy.classroom.models import Homework, School, Event, JoinedEvent, Comment

# Register your models here.

admin.site.register(Homework)
admin.site.register(School)
admin.site.register(Event)
admin.site.register(JoinedEvent)
admin.site.register(Comment)

