from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from study_buddy.members.views import index_no_account, login_user, logout_user, UserRegistrationView

urlpatterns = (
    path('', index_no_account, name='index no_account'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login_user/', login_user, name='login user'),
    path('logout_user/', logout_user, name='logout user'),
)
