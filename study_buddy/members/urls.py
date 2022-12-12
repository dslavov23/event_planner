from django.urls import path

from study_buddy.members.views import index_no_account, register_user, login_user, logout_user
urlpatterns = (
    path('', index_no_account, name='index no_account'),
    path('register/', register_user, name='register'),
    path('login_user/', login_user, name='login user'),
    path('logout_user/', logout_user, name='logout user'),

)
