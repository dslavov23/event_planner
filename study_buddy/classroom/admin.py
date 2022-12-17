from django.contrib import admin
from study_buddy.classroom.models import Event, JoinedEvent, Comment, Location

# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'pk')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address', 'pk')

@admin.register(JoinedEvent)
class JoinedEventAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_c', 'description', 'pk')