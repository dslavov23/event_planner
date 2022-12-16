from django.urls import path, include

from study_buddy.classroom.views import index, dashboard, homework, \
    event_details, event_edit, event_delete, event_add, add_school, profile_details, join_event, my_events, \
    delete_joined_event, search_event, comment_view

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('homework/', homework, name='homework'),
    path('add_event/', event_add, name='add event'),
    path('add_school/', add_school, name='add school'),
    path('comments/<int:pk>', comment_view, name='add comment'),
    path('my_profile/<int:pk>/', profile_details, name='profile details'),
    path('my_events/', my_events, name='my events'),
    path('join_event/<int:pk>',join_event, name='join event'),
    path('delete_joined_event/<int:pk>/', delete_joined_event, name='delete joined event'),
    path('search_event/', search_event, name='search event'),

    path('event/<int:pk>/', include([
        path('details/', event_details, name='event details'),
        path('edit/', event_edit, name='event edit'),
        path('delete/', event_delete, name='event delete'),
    ])))

