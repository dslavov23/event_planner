from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('study_buddy.members.urls')),
    path('', include('study_buddy.classroom.urls')),
]
