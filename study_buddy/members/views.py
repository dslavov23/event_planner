from django.contrib.auth.views import PasswordResetConfirmView
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail, BadHeaderError
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.http import HttpResponse

from study_buddy import settings
from study_buddy.members.forms import UserRegistrationForm
from study_buddy.members.models import AppUser, Profile

User = get_user_model()

def index_no_account(request):
    return render(request, 'index_login_register.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect('index no_account')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There was an error logging in, Try again...")
            return redirect('login user')

    else:
        return render(request, 'users/sign_in.html')


# def register_user(request):
#     if request.method == 'POST':
#         form = ProfileCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, 'Registration successful!')
#             return redirect('index')
#     else:
#         form = ProfileCreateForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'users/sign_up.html', context)


class UserRegistrationView(CreateView):
    # form_class=UserCreationForm
    form_class = UserRegistrationForm
    template_name = 'users/sign_up.html'

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        subject = 'Welcome to Event Planner'
        message = f"Hey {self.request.user.profile.first_name}. Thank you for registering in Event Planner!!"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(self.request, 'Registration successful!')

        return result




def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = 'users/password_reset_email.html'
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Event Planner',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'event.planner.project.django@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="users/password_reset.html",
                  context={"password_reset_form": password_reset_form})



