from django.urls import path, include

from study_buddy.classroom.views import index, dashboard, homework, \
    event_details, event_edit, event_delete, event_add

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('homework/', homework, name='homework'),
    path('add_event/', event_add, name='add event'),

    path('event/<int:pk>/', include([
        path('details/', event_details, name='event details'),
        path('edit/', event_edit, name='event edit'),
        path('delete/', event_delete, name='event delete'),
    ])))
