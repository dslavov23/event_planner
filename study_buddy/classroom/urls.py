from django.urls import path, include


from study_buddy.classroom.views import \
    event_details, event_edit, event_delete, event_add, add_location, join_event, delete_comment_view, \
    delete_joined_event, search_event, comment_view, ProfileDetails, MyEvents, Index, Dashboard

urlpatterns = (
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add_event/', event_add, name='add event'),
    path('add_location/', add_location, name='add location'),
    path('comments/<int:pk>/', comment_view, name='add comment'),
    path('delete_comments/<int:pk>/', delete_comment_view, name='delete comment'),
    # path('my_profile/<int:pk>/', profile_details, name='profile details'),
    path('my_profile/<int:pk>/', ProfileDetails.as_view(), name='profile details'),
    path('my_events/', MyEvents.as_view(), name='my events'),
    path('join_event/<int:pk>/',join_event, name='join event'),
    path('delete_joined_event/<int:pk>/', delete_joined_event, name='delete joined event'),
    path('search_event/', search_event, name='search event'),

    path('event/<int:pk>/', include([
        path('details/', event_details, name='event details'),
        path('edit/', event_edit, name='event edit'),
        path('delete/', event_delete, name='event delete'),
    ])))

